import timeit
from imageai.Prediction.Custom import CustomImagePrediction


def predict(path):
    start = timeit.default_timer()
    prediction = CustomImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("models/" + path)
    prediction.setJsonPath("models/model_class.json")
    prediction.loadModel(num_objects=2)

    (predictions, percentage_probabilities) = prediction.predictImage("stopsign.png", result_count=1)

    print(predictions, " : ", percentage_probabilities)

    end = timeit.default_timer()
    return round((end - start) * 1000)


print(predict("200-32-0.917526.h5"))
print(predict("025-16-0.808889.h5"))
print(predict("model_ex-200_acc-0.833333.h5"))
print(predict("400-16-0.737778.h5"))
print(predict("400-32-0.766667.h5"))


