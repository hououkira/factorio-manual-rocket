from math import ceil

time = 0  # 花费的时间（秒）
machine = set()
machine.add('手搓')
power = 0
technology = set()
assembleTable = {
    # ------------------------------------------最终目标------------------------------------------
    '发射火箭': {
        'material': {
            '火箭组件': 100,
        },
        'time': 0,  # 花费的时间（秒）
        'machine': '火箭发射井',  # 需要的机器，能用就行
        'power': 0,  # 消耗的能量（千焦），手搓不耗能
        'technology': None,  # 需要的科技
    },
    # ------------------------------------------科技包------------------------------------------
    '机自研究包': {
        'material': {
            '铜板': 1,
            '铁齿轮': 1
        },
        'time': 5,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '物流研究包': {
        'material': {
            '基础传送带': 1,
            '电力机械臂': 1
        },
        'time': 6,
        'machine': '手搓',
        'power': 0,
        'technology': '物流研究包',
    },
    '化工研究包': {
        'material': {
            '硫磺': 1,
            '集成电路': 3,
            '内燃机': 2
        },
        'time': 24,
        'machine': '手搓',
        'power': 0,
        'technology': '化工研究包',
    },
    '生产研究包': {
        'material': {
            '铁轨': 10,
            '电炉': 0.33,
            '产能插件1': 0.33,
        },
        'time': 21,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '效能研究包': {
        'material': {
            '处理器': 0.66,
            '机器人构架': 0.33,
            '轻质框架': 1
        },
        'time': 21,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    # ------------------------------------------一般物品------------------------------------------
    '铜板': {
        'material': {
            '铜矿': 1,
        },
        'time': 3.2,
        'machine': '石炉',
        'power': 288.18,  # 游戏中没有说明，经计算得出
        'technology': None,
    },
    '铁板': {
        'material': {
            '铁矿': 1,
        },
        'time': 3.2,
        'machine': '石炉',
        'power': 288.18,
        'technology': None,
    },
    '铁齿轮': {
        'material': {
            '铁板': 2,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '管道': {
        'material': {
            '铁板': 1,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '基础传送带': {
        'material': {
            '铁板': 1,
            '铁齿轮': 1,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '铜线': {
        'material': {
            '铜板': 0.5,
        },
        'time': 0.25,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '电路板': {
        'material': {
            '铁板': 1,
            '铜线': 2
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '电力机械臂': {
        'material': {
            '铁板': 1,
            '铁齿轮': 1,
            '电路板': 1,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '供水泵': {
        'material': {
            '铁齿轮': 1,
            '电路板': 2,
            '管道': 1,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '石炉': {
        'material': {
            '石矿': 5,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '锅炉': {
        'material': {
            '管道': 4,
            '石炉': 1,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 288.18,
        'technology': None,
    },
    '蒸汽机': {
        'material': {
            '铁板': 10,
            '铁齿轮': 8,
            '管道': 5,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 288.18,
        'technology': None,
    },
    '石砖': {
        'material': {
            '石矿': 2,
        },
        'time': 3.2,
        'machine': '石炉',
        'power': 288.18,
        'technology': None,
    },
    '研究中心': {
        'material': {
            '铁齿轮': 10,
            '电路板': 10,
            '基础传送带': 4,
        },
        'time': 2,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '抽油机': {
        'material': {
            '钢材': 5,
            '铁齿轮': 10,
            '电路板': 5,
            '管道': 10,
        },
        'time': 2,
        'machine': '手搓',
        'power': 0,
        'technology': '基础原油处理',
    },
    '炼油厂': {
        'material': {
            '钢材': 15,
            '铁齿轮': 10,
            '电路板': 10,
            '管道': 10,
            '石砖': 10,
        },
        'time': 8,
        'machine': '手搓',
        'power': 0,
        'technology': '基础原油处理',
    },
    '化工厂': {
        'material': {
            '钢材': 5,
            '铁齿轮': 5,
            '电路板': 5,
            '管道': 5,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 0,
        'technology': '基础原油处理',
    },
    '组装机1型': {
        'material': {
            '铁板': 9,
            '铁齿轮': 5,
            '电路板': 3,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 0,
        'technology': '基础原油处理',
    },
    '硫磺': {
        'material': {
            '水': 15,
            '石油气': 15,
        },
        'time': 0.5,
        'machine': '化工厂',  # 化工厂功率217kw，每0.5秒就能制一个硫磺，所以消耗108.5KJ能量
        'power': 108.5,
        'technology': '硫磺',
    },
    '石油气': {
        'material': {
            '原油': 2.22,  # 假设石油气全用基础原油处理制造，不然会很麻烦，涉及到先研究科技之后再升级的问题
        },
        'time': 0.11,
        'machine': '炼油厂',
        'power': 48.2174,  # 炼油厂功率434kw，每0.11秒就能制一个石油气，所以消耗24.11KJ能量
        'technology': None,
    },
    '集成电路': {
        'material': {
            '塑料': 2,
            '铜线': 4,
            '电路板': 2,
        },
        'time': 6,
        'machine': '手搓',
        'power': 0,
        'technology': '高等电学',
    },
    '内燃机': {
        'material': {
            '钢材': 1,
            '铁齿轮': 1,
            '管道': 2,
        },
        'time': 20,  # 用组装机1型，制造速度为0.5
        'machine': '组装机1型',
        'power': 930,
        'technology': '内燃机',
    },
    '钢材': {
        'material': {
            '铁板': 5,
        },
        'time': 16,
        'machine': '石炉',
        'power': 1444.04,
        'technology': '炼钢技术',
    },
    '塑料': {
        'material': {
            '煤矿': 0.5,
            '石油气': 10,
        },
        'time': 0.5,
        'machine': '化工厂',
        'power': 108.5,
        'technology': '塑料',
    },
    '铁轨': {
        'material': {
            '石矿': 0.5,
            '钢材': 0.5,
            '铁棒': 0.5,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 0,
        'technology': '铁路',
    },
    '铁棒': {
        'material': {
            '铁板': 0.5,
        },
        'time': 0.25,
        'machine': '手搓',
        'power': 0,
        'technology': None,
    },
    '电炉': {
        'material': {
            '钢材': 10,
            '集成电路': 5,
            '石砖': 10,
        },
        'time': 5,
        'machine': '手搓',
        'power': 0,
        'technology': '高等冶炼技术2',
    },
    '组装机2型': {
        'material': {
            '钢材': 2,
            '铁齿轮': 5,
            '电路板': 3,
            '组装机1型': 1,
        },
        'time': 0.5,
        'machine': '手搓',
        'power': 0,
        'technology': '自动化2',
    },
    '产能插件1': {
        'material': {
            '电路板': 5,
        },
        'time': 15,
        'machine': '手搓',
        'power': 0,
        'technology': '产能插件',
    },
    '处理器': {
        'material': {
            '电路板': 20,
            '集成电路': 2,
            '硫酸': 5,
        },
        'time': 13.33,
        'machine': '组装机2型',
        'power': 2066.67,
        'technology': '高等电学2',
    },
    '硫酸': {
        'material': {
            '铁板': 0.02,
            '硫磺': 0.2,
            '水': 2,
        },
        'time': 0.02,
        'machine': '化工厂',
        'power': 4.34,
        'technology': '硫磺',
    },
    '机器人构架': {
        'material': {
            '钢材': 1,
            '电池': 2,
            '电路板': 3,
            '电动机': 1,
        },
        'time': 20,
        'machine': '手搓',
        'power': 0,
        'technology': '机器人技术',
    },
    '电池': {
        'material': {
            '铁板': 1,
            '铜板': 1,
            '硫酸': 20,
        },
        'time': 4,
        'machine': '化工厂',
        'power': 868,
        'technology': '电池',
    },
    '电动机': {
        'material': {
            '电路板': 2,
            '内燃机': 1,
            '润滑油': 15,
        },
        'time': 13.33,
        'machine': '组装机2型',
        'power': 2066.67,
        'technology': '电动机',
    },
    '润滑油': {
        'material': {
            '重油': 1,
        },
        'time': 0.1,
        'machine': '化工厂',
        'power': 21.7,
        'technology': '润滑油',
    },
    '重油': {  # 根据我们的手搓精神，另外两种产物被浪费了，不再利用或转化
        # 此外只有需要重油的时候才用高等原油处理配方，其他一律用基础原油处理，不然算起来很麻烦
        'material': {
            '水': 2,
            '原油': 4,
        },
        'time': 0.2,
        'machine': '炼油厂',
        'power': 86.8,
        'technology': None,
    },
    '轻油': {  # 根据我们的手搓精神，另外两种产物被浪费了，不再利用或转化
        # 此外只有需要轻油的时候才用高等原油处理配方，其他一律用基础原油处理，不然算起来很麻烦
        'material': {
            '水': 1.11,
            '原油': 2.22,
        },
        'time': 0.11,
        'machine': '炼油厂',
        'power': 48.22,
        'technology': None,
    },
    '固体燃料': {  # 根据官方的默认配方，用重油造
        'material': {
            '重油': 20,
        },
        'time': 2,
        'machine': '化工厂',
        'power': 434,
        'technology': '基础原油处理',
    },
    '轻质框架': {
        'material': {
            '铜板': 20,
            '钢材': 2,
            '塑料': 5,
        },
        'time': 20,
        'machine': '手搓',
        'power': 0,
        'technology': '轻质框架',
    },
    '速度插件1': {
        'material': {
            '电路板': 5,
            '集成电路': 5,
        },
        'time': 15,
        'machine': '手搓',
        'power': 0,
        'technology': '速度插件',
    },
    '标准混凝土': {
        'material': {
            '铁矿': 0.1,
            '石砖': 0.5,
            '水': 10,
        },
        'time': 13.33,
        'machine': '组装机2型',
        'power': 2066.67,
        'technology': '混凝土',
    },
    '火箭燃料': {
        'material': {
            '固体燃料': 10,
            '轻油': 10,
        },
        'time': 40,
        'machine': '组装机2型',
        'power': 6200,
        'technology': '火箭燃料',
    },
    '火箭控制器': {
        'material': {
            '处理器': 1,
            '速度插件1': 1,
        },
        'time': 30,
        'machine': '手搓',
        'power': 0,
        'technology': '火箭控制器',
    },
    '火箭发射井': {
        'material': {
            '钢材': 1000,
            '处理器': 200,
            '电动机': 200,
            '管道': 100,
            '标准混凝土': 1000,
        },
        'time': 30,
        'machine': '手搓',
        'power': 0,
        'technology': '火箭发射井',
    },
    '火箭组件': {
        'material': {
            '火箭控制器': 10,
            '轻质框架': 10,
            '火箭燃料': 10,
        },
        'time': 3,
        'machine': '火箭发射井',
        'power': 774,
        'technology': '火箭发射井',
    },
}

miningTable = {
    '铜矿': {
        'time': 2,  # 游戏中没有手动开采时间说明，据观察所有矿应该都为2秒
        'machine': '手搓',
        'power': 0
    },
    '铁矿': {
        'time': 2,
        'machine': '手搓',
        'power': 0
    },
    '煤矿': {
        'time': 2,
        'machine': '手搓',
        'power': 0
    },
    '石矿': {
        'time': 2,
        'machine': '手搓',
        'power': 0
    },
    '水': {
        'time': 1 / 1200,  # 抽水所需时间非常小，其实忽略都可以，由于是极限手搓，所以可以直接利用发电用的抽水泵，不用再造抽水泵
        'machine': '供水泵',
        'power': 0
    },
    '原油': {
        'time': 0.1,  # 100%的产率是每秒10个单位
        'machine': '抽油机',
        'power': 9
    },
}

technologyTable = {
    '自动化': {
        'fronts': [],  # 前置科技
        'packages': ['机自研究包'],  # 需要的包类型
        'cost': 10,  # 每种包的花费
        'time': 10  # 研究时间
    },
    '物流学': {
        'fronts': [],
        'packages': ['机自研究包'],
        'cost': 20,
        'time': 15
    },
    '物流研究包': {
        'fronts': [],
        'packages': ['机自研究包'],
        'cost': 75,
        'time': 5
    },
    '炼钢技术': {
        'fronts': [],
        'packages': ['机自研究包'],
        'cost': 50,
        'time': 5
    },
    '基础电学': {
        'fronts': ['自动化'],
        'packages': ['机自研究包'],
        'cost': 30,
        'time': 15
    },
    '物流学2': {
        'fronts': ['物流学', '物流研究包'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 200,
        'time': 30
    },
    '内燃机': {
        'fronts': ['物流研究包', '炼钢技术'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 100,
        'time': 15
    },
    '高等冶炼技术': {
        'fronts': ['物流研究包', '炼钢技术'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 75,
        'time': 30
    },
    '自动化2': {
        'fronts': ['基础电学', '物流研究包', '炼钢技术'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 40,
        'time': 15
    },
    '铁路': {
        'fronts': ['物流学2', '内燃机'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 75,
        'time': 30
    },
    '流体操作': {
        'fronts': ['自动化2', '内燃机'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 50,
        'time': 15
    },
    '混凝土': {
        'fronts': ['自动化2', '高等冶炼技术'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 250,
        'time': 30
    },
    '基础原油处理': {
        'fronts': ['流体操作'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 100,
        'time': 30
    },
    '塑料': {
        'fronts': ['基础原油处理'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 200,
        'time': 30
    },
    '硫磺': {
        'fronts': ['基础原油处理'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 150,
        'time': 30
    },
    '燃料制备': {
        'fronts': ['基础原油处理'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 50,
        'time': 30
    },
    '高等电学': {
        'fronts': ['塑料'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 200,
        'time': 15
    },
    '电池': {
        'fronts': ['硫磺'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 150,
        'time': 30
    },
    '插件': {
        'fronts': ['高等电学'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 100,
        'time': 30
    },
    '化工研究包': {
        'fronts': ['硫磺', '高等电学'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 75,
        'time': 10
    },
    '速度插件': {
        'fronts': ['插件'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 50,
        'time': 30
    },
    '高等电学2': {
        'fronts': ['化工研究包'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 300,
        'time': 30
    },
    '产能插件': {
        'fronts': ['插件'],
        'packages': ['机自研究包', '物流研究包'],
        'cost': 50,
        'time': 30
    },
    '高等原油处理': {
        'fronts': ['化工研究包'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 75,
        'time': 30
    },
    '高等冶炼技术2': {
        'fronts': ['化工研究包', '高等冶炼技术'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 250,
        'time': 30
    },
    '轻质框架': {
        'fronts': ['化工研究包', '高等冶炼技术'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 300,
        'time': 45
    },
    '速度插件2': {
        'fronts': ['速度插件', '高等电学2'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 75,
        'time': 30
    },
    '产能插件2': {
        'fronts': ['高等电学2', '产能插件'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 75,
        'time': 30
    },
    '润滑油': {
        'fronts': ['高等原油处理'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 50,
        'time': 30
    },
    '生产研究包': {
        'fronts': ['产能插件', '高等冶炼技术2', '铁路'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 100,
        'time': 30
    },
    '火箭燃料': {
        'fronts': ['高等原油处理', '燃料制备'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 300,
        'time': 45
    },
    '速度插件3': {
        'fronts': ['速度插件2', '生产研究包'],
        'packages': ['机自研究包', '物流研究包', '化工研究包', '生产研究包'],
        'cost': 300,
        'time': 60
    },
    '电动机': {
        'fronts': ['润滑油'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 50,
        'time': 30
    },
    '产能插件3': {

        'fronts': ['产能插件2', '生产研究包'],
        'packages': ['机自研究包', '物流研究包', '化工研究包', '生产研究包'],
        'cost': 300,
        'time': 60
    },
    '机器人技术': {
        'fronts': ['电动机', '电池'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 75,
        'time': 30
    },
    '效能研究包': {
        'fronts': ['高等电学2', '高等原油处理', '轻质框架'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 100,
        'time': 30
    },
    '火箭控制器': {
        'fronts': ['速度插件', '效能研究包'],
        'packages': ['机自研究包', '物流研究包', '化工研究包'],
        'cost': 100,
        'time': 30
    },
    '火箭发射井': {
        'fronts': ['速度插件3', '火箭控制器', '产能插件3', '火箭燃料', '混凝土'],
        'packages': ['机自研究包', '物流研究包', '化工研究包', '生产研究包', '效能研究包'],
        'cost': 1000,
        'time': 60
    },
}


def make(itemName, num):
    global time
    global power
    if itemName in assembleTable:  # 如果是生产的情况
        print('准备制造' + str(num) + '个' + itemName)
        item = assembleTable[itemName]
        if item['technology'] not in technology and item[
                'technology'] is not None:
            print('需要研发科技：', item['technology'])
            research(item['technology'])  # 研发相应科技
            technology.add(item['technology'])
        if item['machine'] not in machine:
            print('需要制造机器：', item['machine'])
            machine.add(item['machine'])
            make(item['machine'], 1)  # 制造一个相应机器
        print('需要以下材料: ', end='')
        for (key, value) in item['material'].items():
            print(str(int(ceil(value * num))) + '个' + key, end=' ')
        print()
        for key, value in item['material'].items():
            make(key, int(ceil(value * num)))  # 制造所需材料向上取整
        time += item['time'] * num
        power += item['power'] * num
        if (item['machine'] != '手搓'):
            print('用' + item['machine'], end='')
        print('生产' + str(num) + '个' + itemName + '，消耗' +
              str(round(item['time'] * num, 2)) + '秒')
    elif itemName in miningTable:  # 如果是采矿的情况
        item = miningTable[itemName]
        if item['machine'] not in machine:
            print('需要制造机器：', item['machine'])
            machine.add(item['machine'])
            make(item['machine'], 1)  # 制造一个相应机器
        time += item['time'] * num
        power += item['power'] * num
        if (item['machine'] != '手搓'):
            print('用' + item['machine'], end='')
        print('开采' + str(num) + '个' + itemName + '，消耗' +
              str(round(item['time'] * num, 2)) + '秒')
    else:
        raise Exception("未找到目标配方！")


def research(researchName):
    global time
    global power
    print('准备研究科技：' + researchName)
    if '研究中心' not in machine:
        print('需要研究中心进行研究')
        make('研究中心', 1)
        machine.add('研究中心')
    for tech in technologyTable[researchName]['fronts']:
        if tech not in technology:
            print('需要前置科技：', tech)
            research(tech)  # 递归研究前置科技
    for package in technologyTable[researchName]['packages']:
        make(package, technologyTable[researchName]['cost'])  # 制造相应数量的科技包
    second = technologyTable[researchName]['cost'] * technologyTable[
        researchName]['time']
    time += second
    power += 60 * second
    print(researchName + '研究完成！研究共花费' + str(second) + '秒，共消耗' +
          str(60 * second) + 'KJ能量')
    technology.add(researchName)


if __name__ == '__main__':
    print('制造基本电力设施')
    make('供水泵', 1)
    make('锅炉', 1)
    make('蒸汽机', 1)
    machine.update('供水泵', '锅炉', '蒸汽机')
    # 上部分为发电必需设施，如果不需要发电，可以去掉
    make('发射火箭', 1)
    print('总计消耗' + str(round(power, 2)) + 'KJ能量，仅使用煤炭供能，需要开采' +
          str(ceil(power / 40000)) + '个煤矿')
    make('煤矿', ceil(power / 40000))
    print('共计消耗时间：' + str(round(time, 1)) + '秒')
