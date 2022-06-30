from math import ceil

time = 0  # 花费的时间（秒）
machine = set()
machine.add('手搓')
power = 0
technology = set()
assembleTable = {
    '发射火箭': {
        'material': {
            '火箭组件': 100,
        },
        'time': 0,  # 花费的时间（秒）
        'machine': '火箭发射井',  # 需要的机器，能用就行
        'power': 0,  # 消耗的能量（千焦），手搓不耗能
        'technology': None,  # 需要的科技
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
    '铜板': {
        'material': {
            '铜矿': 1,
        },
        'time': 3.2,
        'machine': '石炉',
        'power': 288.18,  # 游戏中没有说明，经计算得出
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
    '铁板': {
        'material': {
            '铁矿': 1,
        },
        'time': 3.2,
        'machine': '石炉',
        'power': 288.18,
        'technology': None,
    },
    '石炉': {
        'material': {
            '石矿': 5,
        },
        'time': 0.5,
        'machine': '石炉',
        'power': 288.18,
        'technology': None,
    },
}

miningTable = {
    '铜矿': {
        'time': 2  # 游戏中没有手动开采时间说明，据观察所有矿应该都为2秒
    },
    '铁矿': {
        'time': 2
    },
    '煤矿': {
        'time': 2
    },
    '石矿': {
        'time': 2
    }
}

technologyTable = {
    '火箭发射井': {
        'fronts': ['速度插件3', '火箭控制器', '产能插件3', '火箭燃料', '混凝土'],  # 前置科技
        'packages': ['机自研究包', '物流研究包', '化工研究包', '生产研究包', '效能研究包'],  # 需要的包类型
        'cost': 1000,  # 消耗多少个研究包
        'time': 60  # 每次需要的时间
    },
}


def make(itemName, num):
    global time
    global power
    if itemName in assembleTable:  # 如果是生产的情况
        item = assembleTable[itemName]
        if item['technology'] not in technology and item[
                'technology'] is not None:
            technology.add(item['technology'])
            research(item['technology'])  # 研发相应科技
            print('需要研发科技：', item['technology'])
        if item['machine'] not in machine:
            print('需要制造机器：', item['machine'])
            machine.add(item['machine'])
            make(item['machine'], 1)  # 制造一个相应机器
        time += item['time'] * num
        power += item['power'] * num
        for key, value in item['material'].items():
            make(key, value * num)
        print('生产' + str(num) + '个' + itemName + '，消耗' +
              str(item['time'] * num) + '秒')
    elif itemName in miningTable:  # 如果是采矿的情况
        item = miningTable[itemName]
        print('开采' + str(num) + '个' + itemName + '，消耗' +
              str(item['time'] * num) + '秒')
        time += item['time'] * num


def research(researchName):
    if '研究中心' not in machine:
        make('研究中心', 1)


def mining(item, num):
    pass


if __name__ == '__main__':
    make('机自研究包', 1)
    print('总计消耗' + str(power) + 'KJ能量，需要开采' + str(ceil(power / 40000)) + '个煤矿')
    make('煤矿', ceil(power / 40000))
    print('共计消耗时间：' + str(time) + '秒')
