from pymongo import MongoClient


class MongoDAO:         #  상단에 두칸씩 띄워주는게 파이선 규칙
    reply_list = []   # MongoDB Document를 담을 List 선언


    def __init__(self):
        # >> MongoDB Connection
        self.client = MongoClient('127.0.0.1', 27017) #클래스 객체 할당(ip, port)
        self.db = self.client['local'] # MongoDb의 'local' DB를 할당
        self.collection = self.db.get_collection('movie') # 동적으로 collection 선택


    def mongo_write(self, data):
        print('>> MongoDB WRITE DATA:)')
        self.collection.insert(data) # JSON Type = Dict Type(Python)

    # MongoDB에서 SelectAll
    def mongo_select_all(self):
        for one in self.collection.find({}, {'_id':0, 'content':1, 'score':1}):
            self.reply_list.append([one['title'], one['content'], one['score']])    #dict에서 Value와 Score만 추출
        return self.reply_list