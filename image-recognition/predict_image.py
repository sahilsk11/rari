import timeit
start = timeit.default_timer()

from imageai.Prediction.Custom import CustomImagePrediction

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("models/model_ex-400_acc-0.737778.h5")
prediction.setJsonPath("models/model_class.json")
prediction.loadModel(num_objects=2)


(predictions, percentage_probabilities) = prediction.predictImage("stopsign.png", result_count=1)

print(predictions, " : ", percentage_probabilities)

end = timeit.default_timer()
print("Time elapsed: " + str(round((end - start) * 1000)) + " ms")