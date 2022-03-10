import matplotlib.pyplot as plt
from dataset_bias import *
from multinomial_pdf import *

BIAS_LIMIT = 5

sex_bias = PDF(distribution_sex, GLOBAL_SEX, len(pkl)) * 100
iqa_sex_bias = max(iqa_sex) - min(iqa_sex)


if (sex_bias > BIAS_LIMIT):
   print("sex_bias: ", sex_bias, ", you are ", (sex_bias - BIAS_LIMIT), "% above the bias limit, data is biased")
else:
   print("sex_bias: ", sex_bias, ", you are ", -(sex_bias - BIAS_LIMIT), "% under the bias limit")

if (iqa_sex_bias > BIAS_LIMIT):
   print("iqa_sex_bias: ", iqa_sex_bias, ", you are ", (iqa_sex_bias - BIAS_LIMIT), "% above the bias limit, data is biased")
else:
   print("iqa_sex_bias: ", iqa_sex_bias, ", you are ", -(iqa_sex_bias - BIAS_LIMIT), "% under the bias limit")

sex_labels = ['Male', 'Female']

fig = plt.figure(1)
#fig.subplots_adjust(hspace = 2.0, wspace = 1.0, left = 0.3)

# sex distribution pie chart
ax1 = plt.subplot(1, 1, 1)
ax1.pie(distribution_sex, labels = sex_labels, autopct="%1.2f%%", startangle=90)
ax1.axis('equal')
plt.show()

# sex iqa pie chart
ax2 = plt.subplot(1, 1, 1)
ax2.pie(iqa_sex, labels = sex_labels, autopct="%1.2f%%", startangle=90)
ax2.axis('equal')

plt.show()