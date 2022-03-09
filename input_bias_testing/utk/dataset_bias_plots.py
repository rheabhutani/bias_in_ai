import matplotlib.pyplot as plt
from dataset_bias import *
from multinomial_pdf import *

BIAS_LIMIT = 5

sex_bias = PDF(distribution_sex, GLOBAL_SEX, len(dir)) * 100
race_bias = PDF(distribution_race, GLOBAL_RACE, len(dir)) * 100
iqa_sex_bias = max(iqa_sex) - min(iqa_sex)
iqa_race_bias = max(iqa_race) - min(iqa_race)


if (sex_bias > BIAS_LIMIT):
   print("sex_bias: ", sex_bias, ", you are ", (sex_bias - BIAS_LIMIT), "% above the bias limit, data is biased")
else:
   print("sex_bias: ", sex_bias, ", you are ", -(sex_bias - BIAS_LIMIT), "% under the bias limit")

if (race_bias > BIAS_LIMIT):
   print("race_bias: ", race_bias, ", you are ", (race_bias - BIAS_LIMIT), "% above the bias limit, data is biased")
else:
   print("race_bias: ", race_bias, ", you are ", -(race_bias - BIAS_LIMIT), "% under the bias limit")

if (iqa_sex_bias > BIAS_LIMIT):
   print("iqa_sex_bias: ", iqa_sex_bias, ", you are ", (iqa_sex_bias - BIAS_LIMIT), "% above the bias limit, data is biased")
else:
   print("iqa_sex_bias: ", iqa_sex_bias, ", you are ", -(iqa_sex_bias - BIAS_LIMIT), "% under the bias limit")

if (iqa_race_bias > BIAS_LIMIT):
   print("iqa_race_bias: ", iqa_race_bias, ", you are ", (iqa_race_bias - BIAS_LIMIT), "% above the bias limit, data is biased")
else:
   print("iqa_race_bias: ", iqa_race_bias, ", you are ", -(iqa_race_bias - BIAS_LIMIT), "% under the bias limit") 

sex_labels = ['Male', 'Female']
race_labels = ['white', 'black', 'asian', 'indian', 'others']

fig = plt.figure(1)
#fig.subplots_adjust(hspace = 2.0, wspace = 1.0, left = 0.3)

# sex distribution pie chart
ax1 = plt.subplot(2, 2, 1)
plt.title('sex distribution')
ax1.pie(distribution_sex, labels = sex_labels, autopct="%1.2f%%", startangle=90)
ax1.axis('equal')

# sex iqa pie chart
ax2 = plt.subplot(2, 2, 2)
plt.title('sex iqa')
ax2.pie(iqa_sex, labels = sex_labels, autopct="%1.2f%%", startangle=90)
ax2.axis('equal')

# race distribution pie chart
ax3 = plt.subplot(2, 2, 3)
plt.title('race distribution')
ax3.pie(distribution_race, labels = race_labels, autopct="%1.2f%%", startangle=90)
ax3.axis('equal')

# race iqa pie chart
ax4 = plt.subplot(2, 2, 4)
plt.title('race iqa')
ax4.pie(distribution_race, labels = race_labels, autopct="%1.2f%%", startangle=90)
ax4.axis('equal')

plt.show()