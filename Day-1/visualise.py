import seaborn as sns 
import matplotlib.pyplot as plt 

sns.set_theme(style ="ticks",  color_codes=True)

kashti = sns.load_dataset("titanic")

p = plt.annotate(x ="sex", data =kashti)
plt.show()
