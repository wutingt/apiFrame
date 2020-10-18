import unittest
import pymysql
import yaml


class ZeusDb(unittest.TestCase):
    # def compare(self, param1, param2):
    #     # 判断Parma1中的元素是否都在parm2里面能够找到，有一个不满足就返回false，否则继续比较下一个字段
    #     for i in param1:
    #         if i not in param2:
    #             return False
    #     # 再判断para2中的元素是否都在parm1里面能够找到，有一个不满足就返回false，否则继续比较下一个字段
    #     for i in param2:
    #         if i not in param1:
    #             return False
    #     return True

    @classmethod
    def setUpClass(cls):

        cls.db_test = pymysql.connect(host="devtest.ibr.cc", port=20215, user="br_zeus", password="BR_zeus123",
                                     db="zeusdb", charset="utf8")
        cls.cursor_test = cls.db_test.cursor()
        # cls.db_test = pymysql.connect(host="devtest.ibr.cc", port=20215, user="br_sdk", password="BR_sdk123",
        #                               db="zeusdb", charset="utf8")  # 20107环境
        # cls.cursor_test = cls.db_test.cursor()
        # cls.db_dba = pymysql.connect(host="localhost",port=5757,user="bonree",password="bonree365",db="zeusdb",charset="utf8")
        # cls.cursor_dba = cls.db_dba.cursor()
        # cls.db_dba = pymysql.connect(host="devtest.ibr.cc", port=20104, user="sdk", password="bonree", db="zeusdb",
        #                             charset="utf8")  # 30035环境
        # cls.cursor_dba = cls.db_dba.cursor()
        cls.db_dba = pymysql.connect(host="devtest.ibr.cc", port=20215, user="br_zeus", password="BR_zeus123", db="zeusdb",
                                     charset="utf8")  # 30035环境
        cls.cursor_dba = cls.db_dba.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cursor_test.close()
        cls.cursor_dba.close()

    def test_t_zeus_sdk_act_process(self):
        self.cursor_test.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_process\");")
        self.columns_test = self.cursor_test.fetchall()
        print('1=======', self.columns_test)
        self.cursor_dba.execute(
            "select FIELD_NAME,VALUE_TYPE,FIELD_TYPE from zeus_metadata_table_field where TABLE_ID IN (select TABLE_ID from zeus_metadata_table where TABLE_NAME=\"t_zeus_sdk_act_process\");")
        self.columns_dba = self.cursor_dba.fetchall()
        print('2=======', self.columns_dba)
        self.result = set(self.columns_test) == set(self.columns_dba)
        self.assertEqual(True, self.result)

        

    def test_yml(self):
        # 读取yaml文件
        with open('C:\\Users\\51102\\Desktop\\123\\info.yaml') as f:
            temp = yaml.load(f.read(), Loader=yaml.FullLoader)
            labels = temp['label_names']
            del labels[0]  # 删除列表第一个元素
        print(labels)

        # 建立一个yaml文件

        with open('C:\\Users\\51102\\Desktop\\123\\iddnfo.yaml', 'w') as ff:
            aproject = {'name': 'Silenthand Olleander',
                        'race': 'Human',
                        'traits': ['ONE_HAND', 'ONE_EYE']
                        }
            yaml.dump(aproject, ff)
            ff.close()
