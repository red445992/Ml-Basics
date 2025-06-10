# binning
Binning is a process of converting continuous numerical data into discrete bins or interval. Imagine you have ages: [17,25,35,41,30]
You could bin them like:
1. 0 - 15: children
2. 15-25 : Teen
3. 25-35 : adult

# Why use binning?
1. Simplifies the model: turns complex continuous data into simple category
2. help handles outliers better
3. can reveal data more clearly especially in descision tree and visualization



# Data Scrubbing
Data scrubbing is a process for fixing error and removing inconsistent or missing values. 

### Why it is important?
1. improves accuracy
2. reduce noises and bias
3. ensures data integrity
4. helps avoid misleading insights

Dirty or messy data can totally confuse your models. Scrubbing helps to make your model trustworthy.

### Steps
1. handling missing values
2. fixing typos and inconsistent data
3. removing duplicates
4. correcting datatypes
5. removing outliers
6. standarizing units


# Qualities of good numerical features
1. clearly named: Features should be human-readable, intuitive, and describe what they measure.
2. Checked and Tested Before Training: Ensure values make sense and aren’t the result of data errors or outliers.
3. Sensible (No Magic Values): Avoid "magic values" like -1, 999, or 0 to represent missing or special cases in continuous data.
4. Handled Properly in Categorical Contexts: For discrete numerical features (e.g., category IDs), explicitly handle missing values with a defined placeholder value.

# polynomial transfrom
A polynomial transform means creating new features by raising an existing numerical feature to a power like squaring, cubing, etc. It's a way to make linear models capable of learning non-linear patterns without switching to a non-linear model.
Why use polynomial transforms?
Some datasets have patterns that can’t be separated or modeled well with a straight line.
 Example: You have two groups of data:
🔴 Red circle
🟢 Green triangles
When plotted, red and green classes can’t be separated with a line, but they can be separated with a curve like: y = x².

That’s where polynomial transforms come in — they let linear models "bend" to fit curves.