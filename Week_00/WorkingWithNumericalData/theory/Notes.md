# Working with Numerical Data
**.** Numerical data - data that can be represented in the form of numerical values. 
    eg: age-17,18,19
        temperature- 33,21
        price - 1000,2000
    Categorial data - data that can be represented in labels or groups or category.
    eg: gender, country, color etc

    Feature Vector - It is a 1-D array of numerical values that represnt characteristics or attributes of a single data point.

    The most common feature engerring techniques are: Normalization and standarization

## How model ingests data with Feature Vectors
It can be understood by following steps:
1. input data collection: eg x1 = [1500,2,1], x2 = [2000,1,2]
2. preprocessing: We do encoding and normalizations in this process.
3. ingestion: Model takes in: 
            i. A matrix X containing all feature vectors : (shape(n_samples,n_features))
            ii. Target array Y containing corresponding labels: shape(n_samples)

4. predict: Now do predictions: model.predict()