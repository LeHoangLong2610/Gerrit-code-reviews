import main

#Test get_code_review():
#Test with different input time interval and scenarios to see if the program crash.
main.get_code_review('2023-02-27','2023-02-27')
main.get_code_review('2023-02-25','2023-02-27')
main.get_code_review('2023-02-28','2023-02-25')
main.get_code_review('test','test')
main.get_code_review('','')


#Test process_json_function():
main.process_json_function('android_review.json') 
main.process_json_function('test1.json') #an empty json file
main.process_json_function('test.json') #a file that doesn't exist
main.process_json_function() #empty agument

#Test export_pdf():
main.export_pdf('android_review.json') 
main.export_pdf('test1.json') #an empty json file
main.export_pdf('test.json') #a file that doesn't exist
main.export_pdf() #empty agument
