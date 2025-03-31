from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def totalhours():
    if request.method=="POST":
        num1 = request.form['num1']
        num2 = request.form['num2']
        
        num1 = num1.split(",")
        num2 = num2.split(",")

        total_hournum1,total_hournum2 = [],[]

        for i in num1:
            i = f"{float(i):.2f}"
            hour_num1 = float(i[:i.find(".")])
            min_num1 = float(i[i.find(".")+1:len(i)])

            if min_num1>=0 and min_num1<15:
                min_num1 = 0

            elif min_num1>=15 and min_num1<45:
                min_num1 = 0.5

            elif min_num1>=45 and min_num1<=59:
                hour_num1 += 1
                min_num1 = 0
            
            total_hournum1.append(hour_num1+min_num1)

        for j in num2:
            j = f"{float(j):.2f}"
            hour_num2 = float(j[:j.find(".")])
            min_num2 = float(j[j.find(".")+1:len(j)])

            if min_num2>=0 and min_num2<15:
                min_num2 = 0

            elif min_num2>=15 and min_num2<45:
                min_num2 = 0.5

            elif min_num2>=45 and min_num2<=59:
                hour_num2 += 1
                min_num2 = 0
            
            total_hournum2.append(hour_num2+min_num2)

        result = sum(total_hournum2) - sum(total_hournum1)
        return render_template("home.html",result=str(result))
    return render_template("home.html")


if __name__ == "__main__":
    app.run('0.0.0.0',debug = True)


