from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    # Setup Spark
    conf = SparkConf().setAppName("WordCount")
    sc = SparkContext(conf=conf)

    # Read input file
    input_file = "/opt/airflow/dags/scripts/book.txt"
    text_file = sc.textFile(input_file)

    # Perform word count
    counts = text_file.flatMap(lambda line: line.split()) \
                      .map(lambda word: (word, 1)) \
                      .reduceByKey(lambda a, b: a + b)

    # Save the result
    output_dir = "/opt/airflow/dags/scripts/output"
    counts.saveAsTextFile(output_dir)
    
    sc.stop()
