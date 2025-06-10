# Conclusion Of this model
A machine learning model health is determined by its data. Feed your model with healthy data and it will thrive; feed you model with junk and its prediction will be worthless.

Best practices for working with numerical data:
1. Remember that you model interacts with data in feature vector, not the data in dataset.
2. Nomralize most numerical features
3. If your normalize method doesnt succedd try different method of normalization.
4. Binning also known as bucket is sometimes better than normalization
5. consider how your data should look like, write verfication tests to validate those expectations. for example
    **.** The absolute value of latitude should never exceed 90. You can write a test to check if a latitude value greater than 90 appears in your data.
6.  Visualize your data with scatter plots and histograms. Look for anamolies
7. Gather statistics not only on the entire dataset but also on smaller subsets of the dataset. That's because aggregate    statistics sometimes obscure problems in smaller sections of a dataset.
8. Document all your data transformations.

Data is your most valuable resource, so treat it with care.