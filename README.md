# GSoC DBpedia: Warm-up Tasks

### Obtain Data on DBpedia

#### Types and Instances

I use sparql query to get five types of instances from the DBpedia. The five types are the subtypes of ```dbo:Artist```:

- dbo:Comedian
- dbo:ComicsCreator
- dbo:FashionDesigner
- dbo:Painter
- dbo:Photographer

The sparql query can be found in ```person.rq```. All the instances are stored in ```data/<TYPE>.txt```.

#### Features

By querying DBpedia, we can get all the yago types of each instance.

The source code can be found in ```data/<TYPE>.py```. All the instances along with features are stored in ```data/<TYPE>Feature.txt```.

### Preprocess the Data

In ```src/processData.py```, I process and clean the data. First, I remove all the instances with no yago type. Then, I use each yago type as features and the five dbo types as labels, whose values are all boolen. Finally, I save them into a single file ```data/data.csv```. There are 6092 instances and 5041 features in the processed dataset.

### Naive SVM Approach

Actually, the problem is a multi-label classification problem. However, we transform the problem to five binary classification problem. For the evaluation, we use 5-fold cross validation on our dataset.

The source code can be found in ```src/svm.py```. The accuracy for each types:
- Comedian: 0.9964
- ComicsCreator: 0.9955
- FashionDesigner: 0.9141
- Painter: 0.9902
- Photographer: 0.9432

It seems pretty good! I think the reason here is that there are not too many types to predict. And this warm-up task can be a intermediate phase in our hierarchical classification.
