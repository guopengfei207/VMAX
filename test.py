fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(1,1,1)
a = [0.91, 2.29, 3]
b = [1.73, 1.99, 4]
c = [2.12, 1.26, 5]
xx = np.array(list(range(3)))
l2 = ax.bar(xx-0.3, a, color='mediumseagreen',align='edge',width=0.2,label='a',yerr=0.1)
l1 = ax.bar(xx-0.1, b, color='indianred',align='edge',width=0.2,label='b',yerr=0.2)
l3 = ax.bar(xx+0.1, c, color='steelblue',align='edge',width=0.2,label='c',yerr=0.3)
ax.set_title("TITLE", fontsize=25, pad=5)
ax.legend(handles=[l1,l2,l3, ], loc=0, ncol=1, fontsize=15, framealpha=0.3)
ax.tick_params(labelcolor='k', labelsize=20, width=3)
# fig.tight_layout() # 调整整体空白
# plt.subplots_adjust(wspace=0.05, hspace=0.15)  # 调整子图间距


plt.xticks([0,1,2], ['label_1','label_2','label_3']) 
plt.show()
