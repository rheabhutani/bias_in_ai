import matplotlib.pyplot as plt
#from dataset_bias import *
#from multinomial_pdf import *

#rep_bias = PDF(distribution, GLOBAL, len(dir)) * 100
#iqa_bias = max(imgQuals) - min(imgQuals)


#if (rep_bias > BIAS_LIMIT):
   # print("rep_bias: ", rep_bias, ", you are ", (rep_bias - BIAS_LIMIT), "% above the bias limit")
#else:
 #   print("rep_bias: ", rep_bias, ", you are ", -(rep_bias - BIAS_LIMIT), "% under the bias limit")

#if (iqa_bias > BIAS_LIMIT):
 #   print("iqa_bias: ", iqa_bias, ", you are ", (iqa_bias - BIAS_LIMIT), "% above the bias limit")
#else:
 #   print("iqa_bias: ", iqa_bias, ", you are ", -(iqa_bias - BIAS_LIMIT), "% under the bias limit")

dist = [45.833333333333336, 54.166666666666664]
iqa = [12.62013041720652, 10.433976408630627]
labels = ['Male', 'Female']

fig = plt.figure(1)
#fig.subplots_adjust(hspace = 2.0, wspace = 1.0, left = 0.3)

# distribution pie chart
ax1 = plt.subplot(2, 1, 1)
plt.title('representation')
ax1.pie(dist, labels = labels, autopct="%1.2f%%", startangle=90)
ax1.axis('equal')

# iqa pie chart
ax2 = plt.subplot(2, 1, 2)
plt.title('iqa')
ax2.pie(iqa, labels = labels, autopct="%1.2f%%", startangle=90)
ax2.axis('equal')
plt.show()