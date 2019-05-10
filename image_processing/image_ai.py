import timeit
start = timeit.default_timer()
from imageai.Prediction.Custom import CustomImagePrediction
import os
execution_path = os.getcwd()
print(execution_path)
prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.setJsonPath(os.path.join(execution_path, "model_class.json"))
prediction.loadModel(num_objects=2)


(predictions, percentage_probabilities) = prediction.predictImage("../images/stopsign.png", result_count=1)

print(predictions, " : ", percentage_probabilities)

end = timeit.default_timer()
print("Time elapsed: " + str(round((end - start) * 1000)) + " ms")