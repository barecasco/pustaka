# Programming with RDDs

An RDD in Spark is simply an immutable distributed collection of objects. Each RDD is split into multiple partitions, which may be computed on different nodes of the cluster.

Once created, RDD offer two types of operations: transformations and actions. Transformations construct a new RDD from a previous one. For example, one common  transformation is filtering data that matches a predicate. In our text file example, we can use this to create a new RDD holding just the strings that contain the word ‘Python’.

Actions, on the other hand, compute a result based on an RDD, and either return it to the driver program or save it to an external storage system (e.g. HDFS). One example of an action we called earlier is first(), which returns the first element in an RDD.

If you are ever confused whether a given function is a transformation or an action, you can look at its return type: transformations returns RDDs, whereas actions return some other data type.
Transformations and actions are different because of the way Spark compute RDDs. Although you can define new RDDs any time, Spark compute them only in a lazy, fashion – that is the first time they are used in an action. This approach might seem unusual at first, but makes a lot of sense when you are working with Big Data. For instance, where we defined a text file and then filtered the lines that include ‘Python’.  If Spark were to load and store all the lines in the file as soon as we wrote the command, it would waste a lot of storage space, given that we then immediately filter out many lines. Instead, once Spark sees the whole chain of transformations, it can compute just the data needed for its result. In fact, for the first() action, Spark scans the file only untul it finds the first matching line; it doesn’t even read the whole file.

Finally, Spark’s RDDs are by default recomputed each time you run an action on them. If you would like to reuse an RDD in multiple actions, you can ask Spark to persist it in using `RDD.persist()`. We can ask Spark to persist our data in a number of different places.  After computing it the first time, Spark will store the RDD contents in memory partitioned accross the machines in your cluster), and reuse them in future actions. Persisting RDDs on disk instead of memory is also possi-ble. The behavior of not persisting by default might again seem unusual, but it makes a lot of sense for big datasets. If you will not reuse the RDD, there is no reason to waste storage space when Spark could in-stead stream through the data once and just compute the result.

In practice, you will often use persist to load a subset of your data into memory and query it repeatedly. For example, if we knew that we wanted to compute multiple results about the README lines that con-tain Python, we could write the script below:

```
>>> pythonLines.persist
>>> pythonLines.count()
2
>>> pythonLInes .first()
‘Interactive python shells’
```

Every Spark program and shell session will work as follows:
1.	Create some input RDDs from external data.
2.	Transform them to define new RDDs using transformations like filter()
3.	Ask Spark to persist any intermediate RDDs that will need to be reused.
4.	Launch actions such as count and first to kick off a parallel computation, which is then optimized and executed by Spark.

## Creating RDDs

Spark provides two ways to create RDDs:
1.	Loading an external dataset
2.	Parallelizing a collection in your driver program.
The simplest way to create RDDs is to take an existing collection in your program and pass it to `SparkContext.parallelize` method.
