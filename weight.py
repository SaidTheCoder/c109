import csv
import pandas as pd
import statistics
df=pd.read_csv("height-weight.csv")
weight_list=df["Weight(Pounds)"].tolist()

weight_mean=statistics.mean(weight_list)
weight_median=statistics.median(weight_list)
weight_mode=statistics.mode(weight_list)
weight_std_deviation=statistics.stdev(weight_list)

print("mean,median,mode and standard deviation of the weight is {},{},{} and {} respectivly".format(weight_mean,weight_median,weight_mode,weight_std_deviation))

weight_first_std_deviation_start, weight_first_std_deviation_end=weight_mean-weight_std_deviation,weight_mean+weight_std_deviation
weight_second_std_deviation_start, weight_second_std_deviation_end=weight_mean-(2*weight_std_deviation),weight_mean+(2*weight_std_deviation)
weight_third_std_deviation_start, weight_third_std_deviation_end=weight_mean-(3*weight_std_deviation),weight_mean+(3*weight_std_deviation)

weight_list_of_data_within_1_std_deviation= [result for result in weight_list if result>weight_first_std_deviation_start and result<weight_first_std_deviation_end]
weight_list_of_data_within_2_std_deviation= [result for result in weight_list if result>weight_second_std_deviation_start and result<weight_second_std_deviation_end]
weight_list_of_data_within_3_std_deviation= [result for result in weight_list if result>weight_third_std_deviation_start and result<weight_third_std_deviation_end]

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviations".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviations".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))
