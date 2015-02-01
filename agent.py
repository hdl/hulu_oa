import sys, traceback

class Chart:
    def __init__(self):
        self.info_dict = {}      #key is name, value is information list
        self.children_dict = {}  #key is boss, value is worker name list
        self.case_output=''

    def level2dash(self,level):
        dash=""
        for i in range(level):
            dash = dash +'-'
        return dash

    def dfs(self, boss_name, level):
        if self.children_dict.has_key(boss_name):
            self.children_dict[boss_name].sort()
            for employee_name in self.children_dict[boss_name]:
                self.case_output += self.level2dash(level) + employee_name + " (" + self.info_dict[employee_name][2] + ") "+ self.info_dict[employee_name][3] +"\n"
                self.dfs(employee_name, level+1)
        else:
            return


    def fun(self, info_list):
        for employee in info_list:
            name, boss, title, year = employee.split(',')
            self.info_dict[name] = [name, boss, title, year]
            if boss in self.children_dict:
                self.children_dict[boss].append(name)
            else:
                self.children_dict[boss] = []
                self.children_dict[boss].append(name)
        self.case_output=''
        self.dfs('NULL', 0)
        print self.case_output
        return self.case_output
        


def main():

    with open("input.in", "r") as reader:
        with open("output.out", "w") as writer:
            reader.readline() #skip first line
            for case_num, line in enumerate(reader, 1):
                chart  = Chart()
                info_list = line.rstrip().split('--')
                writer.write("Case #%d\n" % case_num)
                writer.write(chart.fun(info_list))

if __name__ == '__main__':
    main()

