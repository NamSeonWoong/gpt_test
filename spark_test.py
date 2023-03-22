# PySpark 모듈을 임포트합니다.
from pyspark.sql import SparkSession

# SparkSession 객체를 생성합니다.
spark = SparkSession.builder.appName("example").getOrCreate()

# 데이터를 로드합니다.
data = spark.read.text(r"C:\Users\mindslab\PycharmProjects\XDC\environment_eval\환경2023\환경영향평가_협의의견.csv")

# 데이터를 처리합니다.
result = data.filter(data.value.contains("example"))

# 결과를 출력합니다.
result.show()

# SparkSession 객체를 종료합니다.
spark.stop()