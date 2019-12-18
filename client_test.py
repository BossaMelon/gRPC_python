import random
import time

import grpc
from protos.compiled import krc_grpc_pb2_grpc
from protos.compiled import krc_grpc_pb2


def run():
    channel = grpc.insecure_channel('localhost:30002')

    stub = krc_grpc_pb2_grpc.CrLearningServiceStub(channel)

    # response = stub.StartInference(krc_grpc_pb2.StartInferenceParams())
    # train = stub.StartTraining(krc_grpc_pb2.StartTrainingParams())
    # print(train.accuracy)
    # if response.success:
    #     print("Connected")

    while True:
        mode = int(input('''Choose mode: 
1:detect, 2:labeling, 3:train, 4:delete data
'''))

        if mode == 1:
            detect_response = stub.StartInference(krc_grpc_pb2.StartInferenceParams())
            if detect_response.success:
                print('Connected, waiting for live data')
                print()
                while True:
                    result = stub.RequestInference(krc_grpc_pb2.RequestInferenceResult())
                    if result.success:
                        print('Class: ' + str(result.inference_class))
                        print('Possibility: ' + str(result.probability))
                        print(40 * '-')

                        time.sleep(0.05)
                    else:
                        print("detection fail...")
            else:
                print("Connection fail")

        if mode == 2:
            labeling_response = stub.StartLabeling(krc_grpc_pb2.StartLabelingParams())
            for i in range(20):
                label = random.randint(0, 1)
                stub.LabelTrace(krc_grpc_pb2.LabelTraceParams(process_name="try_file", trace_id=-1, label_class=label))

        if mode == 3:
            train_response = stub.StartTraining(krc_grpc_pb2.StartTrainingParams())
            print(train_response.accuracy)
        if mode == 4:
            delete_response = stub.DeleteData(krc_grpc_pb2.DeleteDataParams())


if __name__ == '__main__':
    run()
