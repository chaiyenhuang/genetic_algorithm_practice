

# import statistics
from statistics import *
from numpy import *
from random import *


# 0 日班
# 1 夜班
# 2 大夜班
# 3 放假
# 4 休假


CROSSOVER_RATE = 0.5
MUTATION_RATE = 0.1
ITERATION_TIME = 5     #迭代次數

NUMBER_OF_GENETIC = 10   #基因數量
NUMBER_OF_WORKER = 17    #工作人數

# 染色體集合
all_genetic = []
best_genetic = []

def targetFunction(teamSchedule):
  # O -> 休假次數
  # µ0 -> 平均休假次數
  # 變異數
  day_shift = [] #日班
  later_shift = []
  grave_shift = []
  for i in range(NUMBER_OF_WORKER):
    # 日班
    day_shift.append(len([i for i in teamSchedule[i] if i == 0]))
    # 夜班
    later_shift.append(len([i for i in teamSchedule[i] if i == 1]))
    # 大夜班
    grave_shift.append(len([i for i in teamSchedule[i] if i == 2]))

  # print('day_shift: ',day_shift)
  target_value = round(variance(day_shift)+variance(later_shift)+variance(grave_shift), 10)
  print('Total variance: ', target_value )


# 單點交配
def crossover():
  # 隨機取兩個個體
  first = int(random() * (NUMBER_OF_GENETIC))-1
  second = int(random() * (NUMBER_OF_GENETIC))-1
  while(first==second):
    second = int(random() * (NUMBER_OF_GENETIC))-1

  crossover_genetic_1 = all_genetic[first]
  crossover_genetic_2 = all_genetic[second]

  crossover_if = random()
  if( crossover_if > CROSSOVER_RATE):
    # 不交配
    return 1
  else:
    # 取第幾個工人
    crossover_worker = int(random() * (NUMBER_OF_WORKER-1) )
    # 取工人第幾天的工作
    crossover_date = int(random() * (28-1) )

    for i in range(crossover_date):
      temp = crossover_genetic_1[crossover_worker][i]
      crossover_genetic_1[crossover_worker][i] = crossover_genetic_2[crossover_worker+1][i]
      crossover_genetic_2[crossover_worker+1][i] = temp

    # 取得突變位置
  return 1

# 每個染色體隨意找地方把一個值改成另一個
def muation():
  pass

def generateEachWorker():
  each_worker = []

  workDay = 0
  holiday = 0 #放假
  vacation = 0 #休假
  for i in range(4):
    for j in range(7):

      if(holiday>=2):
        work_type = int(random() * 3)
      else:
        work_type = int(random() * 4)
        if(work_type==3):
          holiday+=1
        else:
          workDay+=1
      each_worker.append(work_type)

    holiday=0
  return each_worker


def generateGenetic():
  one_genetic = []
  for i in range(NUMBER_OF_WORKER):
    one_genetic.append(generateEachWorker())
  return one_genetic

def main():
  for i in range(NUMBER_OF_GENETIC):
    all_genetic.append( generateGenetic() )
      
  for i in range(ITERATION_TIME):
    print('============= ', (i+1) ,' =============')
    for j in range(NUMBER_OF_GENETIC):
      targetFunction(all_genetic[j])
      crossover()

if __name__ == "__main__":
    main()