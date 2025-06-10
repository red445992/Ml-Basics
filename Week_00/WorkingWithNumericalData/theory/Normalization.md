# Normalization
Normalization is a process of converting datas of different range into a comparable range with other columns so that model can get high accuracy. It helps model converge more quickly during training. It helps model infer for better prediction and also help the model to learn appropriate weights for each features.

**.** Note: If you want to normalize a feature during training you must also normalize that feature when making predictions.

There are different methods of normalization. They are :
1. linear scaling
2. Zscore
3. Log scaling
-> clipping also is used to tame unruly numerical features into range that produce better models but it is not a normalization technique/

### Linear Scaling
It transforms your data into a specific range most commonly 0 to 1. It is also called Min Max scaling. Xscaled = (x-xmin)/(xmax-xmin))

***.*** When to use Linear scaling?
1. you need features on the same scale
2. you know the min and max values
3. your data is not skewed

***.*** when not to use linear scaling? 
1. your data has outliers.
2. you dont want to loose distribution shape.

Checkout linear_scaling programming implementaion- [Normalization](/WorkingWithNumericalData/code/Normalization.ipynb)

### Z score
It is used to compare values that come from different distributions or scale.
z_score = (X-Mean)/SD

***.*** When to use Z Score
1. data follows a gaussian distribution
2. you want features to have equal importance
3. you are using ML algorithms that assume normality

***.*** when to avoid:
1. the data is heavily skewed or has outliers that distort mean and SD.
Checkout Z_score programming implementaion- [Normalization](/WorkingWithNumericalData/code/Normalization.ipynb)



### Log scaling
This helps you transform your data using logarithmic function. It compress the large value and strach small values. It helps to visualize skewed data. It handle outliers. It helps to improve performance of models sensitive to variace.

    Xscaled = log(x)
**.** when to use:
1. data is heavily right skewed
2. features span several magnitudes
3. you want to reduce variance and outliers

**.** avoid when:
1. data contains 0 or negative values
2. you need to preserve absolute differences

Checkout Z_score programming implementaion- [Normalization](/WorkingWithNumericalData/code/Normalization.ipynb)




# clipping
Clipping is a technique used to limit extreme values in your data to a defined minimum or maximum. It's commonly used to reduce the effect of outliers during model training.

### Why clip?
1. Outliers (extremely high or low values) can distort:
2. Statistics like the mean or standard deviation
3. The learning process of many ML models, especially linear models

## How It Works:
Let’s say you have a feature (column) in your dataset: roomsPerPerson.
Most values are between 0 and 4, but a few extreme values go up to 17, which makes the data skewed.
Clipping means:
If a value is greater than 4, replace it with 4.
If a value is less than 0, replace it with 0 (if clipping lower bound too).
 After clipping, all values are within the range [0, 4].