from base import meetings_to_reschedule

Test1 = [[0,1],[0],[1]] 
meetings_to_reschedule(Test1)

Test2 = [[0,1,2],[2,3]] 
meetings_to_reschedule(Test2)

Test3 = [[4,10],[3,4,12],[0,8,9,10,13],[1,5,7],[2,6],[9,4,10,11,12],[11,13]] 
meetings_to_reschedule(Test3)

Test4 = [[6,16,17],[8,9],[1],[7,14,9],[10,5],[2,7],[0,6,7,9],[10,11,5,13,15,16,17],[7,9],[5,9],[2,12,5,6,14,7,15,9],[10,5,14],[1,4,8],[1,3,9],[5]] 
meetings_to_reschedule(Test4)

Test5 = [[9,16,34],[10,13,18,20,23,28,30,31,32],[4,7,8,11,16,17,19,25,29,36,37],[0,2,23,28],[1,3,7,8,14,15,19,24,25,26,32],[12,28],[16,21,24,33,34],[5,6,10,15,16,17,21,22,24,27,33,34,35]] 
meetings_to_reschedule(Test5)

Test6 = [[55,2],[34,66,60],[15,9,12,82],[39,51,81],[65,69,70],[67,47,58,10,62],[30],[36,7],[0,16],[75,2,20,43],[37,38,44],[34,56,46,79],[26,11,72],[67,47],[16,50],[72],[12],[16,63],[60,18],[64,16],[16,63],[32],[34,16],[16,8],[16,8],[2,3,4,49,52,54,55,75,14,76,22,41,43],[57,30],[64,80,23],[64,69,30],[2,49],[48,16,53],[16,63],[5,16],[69,70],[34,65,69,38,6,30,17],[25,77,59,71,78,19,21,40,12,24],[34,16],[55,66,5,60],[27,14,5,46,76,49],[33,28,69],[25,77,59,71,78,19,40,21,12,24],[5,29],[32],[28,16],[2,14],[37,69,6,30,17,31,73],[32,1,42],[64,26,60,11],[16,13],[16,8],[34,16],[16,44],[9,83],[45,81],[46,76],[46,8,39,51],[8,54],[16,50],[74,81,53],[5,16],[61,23],[65,68,77,81],[74,35,37,6,17]] 
meetings_to_reschedule(Test6)

Test7 = [[71,61,26],[72,75,76],[73,54,64,10,68],[88,56,69],[71,17,8],[18],[40,17,66,47,13],[40,62,52,88],[11,79,36,58,15],[17,67],[33],[38],[3,4,5,55,59,60,61,82,18,85,26,48,50],[17,84],[74,83,43],[71,89,27],[11,79,46,58],[34,33],[71,75,35],[66,14],[72,33],[75,76],[19,77,27],[40,72,75,44,7,35,20],[18,34],[71,17,33,67],[29,86,65,78,87,22,23,47,16,28],[38,37,27],[30,18,6,52,85,55],[79,28,58],[17,88,69],[76,23],[39,32,75],[29,86,65,78,87,22,47,23,16,28],[11,79,58],[21,88,51],[38],[61,88],[3,18],[39,0,24,23],[33,70],[42,75,7,35,20,37,80],[38,1,49],[31,12,88],[39,40,43],[33,56],[33,25],[33],[2,56],[52,85],[52,9,45,57],[53,33],[66,27],[63,88],[81,41,42,7,20]]
meetings_to_reschedule(Test7)
