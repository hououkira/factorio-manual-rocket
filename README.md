# factorio manual rocket
 你有没有考虑过在异星工厂里手搓一个火箭通关需要花费多少时间？这个程序能满足你的幻想！当然计算其他物品的纯手搓时间也是可以的，欢迎想手搓通关的人小伙伴进行参考~~

 V1.0.0简介
程序已经完成，计算出的手搓火箭通关时间为4518509.8秒，此时间基于以下规则：
1.能手搓的东西都手搓，不能手搓的东西，就用一个最差的能制造此物品的机器进行制造，例如炼油用一个炼油厂，化工用一个化工厂不必多说，只有生产电动机、处理器、标准混凝土之类的要用液体的才用组装机2型，其他全用1型。
2.在使用机器的时间也不重叠计算，例如现在正在用组装机1型制造物品，此时也不能手搓物品，只能看着组装机进行制造。其他机器同理。机器和机器之间也不能重叠时间，也就是说你只能同时使用一个制造机器。
3.有一些东西需要额外制造，已经写在程序的注释中，目前有一个抽水机，一个锅炉和一个蒸汽机用来供电，一个蒸汽机足够满足所有单个机器的用电了。直接将上述几个部件进行连接，所以不需要额外的管道。
4.目前肯定还有很多很多误差，bug，以及数据录入失误以及未考虑的制造情况之类的，欢迎大家多多脑洞，把时间优化的更精确一些

