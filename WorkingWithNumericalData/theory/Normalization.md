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

