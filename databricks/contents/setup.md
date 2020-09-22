# Spark Setup

### Downloading Spark {#sparkdown}

Start by downloading a recent precompiled released version of Spark. Visit

http://spark.apache.org/downloads.html

Select the package type of Prebuilt for Hadoop 2.7 and later. If you have an existing Hadoop cluster or HDFS installation, download the matching version. In Windows you can unpack the tar file with 7-zip.

`bin` folder contains executables that can be used to interact with Spark in various ways. `examples` contains some helpful Spark standalone jobs that you can look at and run to learn about the Spark API.

### Install Spark on Windows {#sparkwin}

Take heed this [guide](https://bigdata-madesimple.com/guide-to-install-spark-and-use-pyspark-from-jupyter-in-windows/).

1. Install Java
2. Set root folder location, me myself set it in `D:/spark`.
3. Create new folder `./hadoop/bin`.
4. Find and download `winutils.exe` to be put inside `./hadoop/bin`.
5. Add new environment variables: `SPARK_HOME`, `HADOOP_HOME`, and `PYTHONPATH` in a temporary one time init batch script:

```
@echo off
echo setting spark_home and hadoop_home environment variables...
set SPARK_HOME=D:\spark\spark-3.0.0-bin-hadoop2.7
set HADOOP_HOME=D:\spark\spark-3.0.0-bin-hadoop2.7\hadoop
set PYTHONPATH=%SPARK_HOME%\python;%SPARK_HOME%\python\lib\py4j-0.10.9-src.zip;
```

### Using Spark Shell {#sparkshell}
To use the shell, you can go to `%SPARK_HOME%\bin` and run `pyspark`.

At a high level, every Spark application consists of a *driver program* that launches various parallel operations on a cluster. The driver program contains your application's main function and defines distributed datasets on the cluster, then applies operations to them. In our case, the driver program was he Spark shell itself, and you could just type in the operations you wanted to run.

Driver programs access Spark through a ``SparkContext`` object, which represents a connection to a computing cluster.  In the shell, a ``SparkContext`` is automatically created for you as the variable called ``sc``. Once you have a `SparkContext`, you can use it to build RDDs.

### Using Spark in Jupyter {#sparkjup}

**Important**. The correct pyspark to install is the one come along with the Spark itself (inside the `bin`).

The Python package `findspark` should be used to run the Spark in notebook environment, though sometime if the environment variables is set up correctly you may not need to use the package. Below is simple example of using Spark in notebook:

```
import findspark
findspark.init()
import pyspark
import random
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Agra Spark").getOrCreate()
sc = spark.sparkContext
```

### Standalone Spark {#sparkalone}

Apart from running interactively, Spark can be linked into standalone applications in Python. The main difference from using it in the shell is that you need to initialize your own `SparkContext`, like in the notebook. After that, the API is the same.

The process of linking to Spark varies by language. In Python, you simply write applications as Python scripts, but you must run them using the `bin/spark-submit` script included in Spark. The `spark-submit` script includes  the spark dependencies for us in Python. This script sets up the environment for Spark’s Python API to function. Simply run your script with the line given :

`bin/spark-submit my_script.py`

In standalone you must create your own `SparkContext`, see example below:

```
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("AgraApp")
sc = SparkContext(conf = conf)
```

Upon creating a `SparkContext`, you passed two parameters:

+ A cluster URL. `"local"` in the above example means asking Spark to run one thread on the local machine, without connecting to the cluster. We can add more thread by appending the number of the threads: `"local(3)"` will use 3 threads in parallel.
+ An application name, namely `"AgraApp"`. This will identify your application on the cluster's manager's UI if you connect to a cluster.

### Shutting Down Spark {#sparkshut}
To shut down Spark, you can either call the `stop()` method on your `SparkContext`, or simply exit the application.
