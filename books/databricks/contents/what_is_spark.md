# What is Spark?
Spark is a cluster computing platform designed to be fast and general-purpose. It extends the popular `MapReduce` Model to efficiently support more types of computations, including interactive queries and stream processing.

##### *Fast*
Spark has the ability to run computations in memory while it is more efficient than `MapReduce` for complex applications running on disk.

#####*General*
Spark is designed to cover a wide range of workloads that previously requireed separate distribute systems, including batch ap-plications, iterative algorithm (for ML), interactive queries and streaming.

#####*Unified*
Spark is designed to support a wide range of data analytics tasks, ranging from simple data loading and SQL queries to machine learning and streaming computation, over the same engine and with a consistent set of APIs.

### Spark for Data Scientist

Data Scientist is somebody whose main task is to analyze and model data. DS have experience  with techniques necessary to transform data into formats that can be analyzed for insights (data wrangling).

DS use their skills to analyze data with the goal of answering a question or discovering insights. Their workflow involve ad hoc analysis, so they use interactive shells (instead of building complex applications) that let them see results of queries and snippets of code in the least amount of time. Spark speed and simple API shine for this purpose, and its built in libraries mean that many algorithms are available out of the box.

Spark supports the different tasks of data science with a number of components. The Spark shell makes it easy to do interactive data anal-ysis using Python. Spark SQL also has a separate SQL shell that can be used to do data exploration using SQL, or Spark SQL can be used as part of a regular Spark program or in the Spark shell. Machine learning and data analysis is supoorted through the MLLib libraries. In addition, there is support for calling out to external programs in Matlab or R. Spark enables data scientists to tackle problems with larger data sizes than they could before with tools like R or Pandas.

The work of a data scientist will be productized or extended, hardened and tuned to become a production data processing application, which itself is a component of a business application. For example, the initial investigation of a data scientist might lead to the creation of a produc-tion recommender system that is integrated into a web application and used to generate product suggestions to users. Often it is a different person or team that leads the process of productizing the work of the data scientists, and that person is often an engineer.

### Spark for Data Processing applications

We think of engineers as a large class of software developers who use Spark to build production data processing applications. These devel-opers usually have an understanding of the principles of software en-gineering, such as encapsulaion, interface design, and object-oriented programming. They frequently have a degree in computer science. They use their engineering skills to design and build software systems that implement a business use case.

Spark provides a simple way to parallelize these applications across clusters, and hides the complexity of distributed systems program-ming, network communication, and fault tolerance. The system give them enough control to monitor, inspect, and tune applications while allowing them to implement common tasks quickly. The modular na-ture of the API makes it easy to factor work into reusable libraries and test it locally.

Spark’s users choose it to use for their data processing applications because it provides a wide variety of functionality, is easy to learn and use, and is mature and reliable.
