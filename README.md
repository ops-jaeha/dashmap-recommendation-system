# dashmap-recommendation-system
dashmap 프로젝트의 강좌 추천 시스템이다.

## Model
 Contents based recommender system을 사용할 계획이다.  
컨텐츠 기반 필터링은 고객이 과거 만족한 상품을 추출하고, 추출된 상품과 유사도가 높은 아이템을 선정하여 추천한다.

## Installation
### Docker
```
$ git clone https://github.com/dash-map/dashmap-recommendation-system
$ cd dashmap-recommendation-system

$ docker pull taki0412/dashmap-recommender
$ docker run -it -d -p 8080:8080 --name "name" taki0412/dashmap-recommender
```
### Quick Start
```
$ git clone https://github.com/dash-map/dashmap-recommendation-system
$ cd dashmap-recommendation-system

$ pip3 install -r requirements.txt
```