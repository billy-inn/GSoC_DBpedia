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



