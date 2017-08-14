#-*- coding: utf-8 -*-　　
#-*- coding: cp950 -*-　
from chatterbot import ChatBot
import time
from chatterbot.trainers import ChatterBotCorpusTrainer
deepThought = ChatBot("deepThought",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.synset_distance"
        }
    ],
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
     database='chatterbot-database',
     database_uri='mongodb://root:root@127.0.0.1:27017',
     
)
deepThought.set_trainer(ChatterBotCorpusTrainer)
# 使用中文语料库训练它
deepThought.train("/root/star/")  # 语料库
tStart = time.time()
print(deepThought.get_response("抓我的手"))
tEnd = time.time()
print(tEnd - tStart)
# print(deepThought.get_response("生命、宇宙以及世间万物的终极答案是什么?"))
