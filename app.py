from asyncio.windows_events import NULL
from flask import Flask, render_template, request, url_for, redirect, session
from flask import Markup
import os
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import pickle
from sklearn.metrics import accuracy_score
import numpy as np

arr = []

app = Flask(__name__)

app.secret_key = 'your secret key'

  
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yashnage'
app.config['MYSQL_DB'] = 'trial1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)


u = ""
myresult = 0
myresult1 = 0
f = int(0)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT * FROM register WHERE email = % s AND password = % s', (email, password, ))
        pred_data = cur.fetchone()

        if pred_data:
            session['loggedin'] = True
            session['id'] = pred_data['id']
            session['email'] = pred_data['email']
            session['username'] = pred_data['username']


            msg = 'Logged in successfully !'
            cur.execute('select id from register where email = %s', (email, ))
            myresult = cur.fetchone()
            u = email
            print("email is :", u)
            f = (myresult['id'])

            print("checki 1", f)
            print(f)
            print(type(f))
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect email / password !'
    return render_template('login.html', msg=msg)


@app.route('/register', methods=['POST', 'GET'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM register WHERE username = % s', (username, ))
        pred_data = cursor.fetchone()
        if pred_data:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO register VALUES (NULL, % s, % s, % s)', (username, password, email))

            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)


@app.route('/results', methods=['GET'])
def results():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM history WHERE id = % s and test1=1',(session['id'], ))
        msg = cur.fetchall()
        if msg:
            return render_template('history.html', msg=msg)
        else:
            msg = 'Invalid results !'
        return render_template('history.html', msg=msg)


@app.route('/logout',  methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/happy')
def happy():
    return render_template('happy.html')


@app.route('/sad')
def sad():
    return render_template('sad.html')


@app.route('/angry')
def angry():
    return render_template('angry.html')


@app.route('/predict', methods=['GET', 'POST'])
def send():
    if request.method == 'GET':
        return render_template('app.html')
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        BFI_EXT_1 = request.form['BFI_EXT_1']
        BFI_AGR_1 = request.form['BFI_AGR_1']
        BFI_CON_1 = request.form['BFI_CON_1']
        BFI_NEU_1 = request.form['BFI_NEU_1']
        BFI_OPEN_1 = request.form['BFI_OPEN_1']
        BFI_EXT_2 = request.form['BFI_EXT_2']
        BFI_AGR_2 = request.form['BFI_AGR_2']
        BFI_CON_2 = request.form['BFI_CON_2']
        BFI_NEU_2 = request.form['BFI_NEU_2']
        BFI_OPEN_2 = request.form['BFI_OPEN_2']
        BFI_EXT_3 = request.form['BFI_EXT_3']
        BFI_AGR_3 = request.form['BFI_AGR_3']
        BFI_CON_3 = request.form['BFI_CON_3']
        BFI_NEU_3 = request.form['BFI_NEU_3']
        BFI_OPEN_3 = request.form['BFI_OPEN_3']
        BFI_EXT_4 = request.form['BFI_EXT_4']
        BFI_AGR_4 = request.form['BFI_AGR_4']
        BFI_CON_4 = request.form['BFI_CON_4']
        BFI_NEU_4 = request.form['BFI_NEU_4']
        BFI_OPEN_4 = request.form['BFI_OPEN_4']
        BFI_EXT_5 = request.form['BFI_EXT_5']
        BFI_AGR_5 = request.form['BFI_AGR_5']
        BFI_CON_5 = request.form['BFI_CON_5']
        BFI_NEU_5 = request.form['BFI_NEU_5']
        BFI_OPEN_5 = request.form['BFI_OPEN_5']
        BFI_EXT_6 = request.form['BFI_EXT_6']
        BFI_AGR_6 = request.form['BFI_AGR_6']
        BFI_CON_6 = request.form['BFI_CON_6']
        BFI_NEU_6 = request.form['BFI_NEU_6']
        BFI_OPEN_6 = request.form['BFI_OPEN_6']
        BFI_EXT_7 = request.form['BFI_EXT_7']
        BFI_AGR_7 = request.form['BFI_AGR_7']
        BFI_CON_7 = request.form['BFI_CON_7']
        BFI_NEU_7 = request.form['BFI_NEU_7']

        BFI_OPEN_7 = request.form['BFI_OPEN_7']
        BFI_EXT_8 = request.form['BFI_EXT_8']
        BFI_AGR_8 = request.form['BFI_AGR_8']
        BFI_CON_8 = request.form['BFI_CON_8']
        BFI_NEU_8 = request.form['BFI_NEU_8']
        BFI_OPEN_8 = request.form['BFI_OPEN_8']
        BFI_OPEN_9 = request.form['BFI_OPEN_9']
        BFI_AGR_9 = request.form['BFI_AGR_9']
        BFI_CON_9 = request.form['BFI_CON_9']
        BFI_OPEN_10 = request.form['BFI_OPEN_10']

        arr.clear()
        filename = "PP_reg.sav"
        loaded_model = pickle.load(open(filename, 'rb'))
        arr.append(num1)
        arr.append(num2)
        extra_score = int(BFI_EXT_1) + int(BFI_EXT_3) + int(BFI_EXT_4) + int(BFI_EXT_6) + \
            int(BFI_EXT_8) + 12 - int(BFI_EXT_2) - \
            int(BFI_EXT_5) - int(BFI_EXT_7)
        print(extra_score)
        agre_score = int(BFI_AGR_2) + int(BFI_AGR_4) + int(BFI_AGR_5) + int(BFI_AGR_7) + int(
            BFI_AGR_9) + 16 - int(BFI_AGR_1) - int(BFI_AGR_3) - int(BFI_AGR_6) - int(BFI_AGR_8)
        print(agre_score)
        con_score = int(BFI_CON_1) + int(BFI_CON_3) + int(BFI_CON_6) + int(BFI_CON_7) + int(
            BFI_CON_8) + 16 - int(BFI_CON_2) - int(BFI_CON_4) - int(BFI_CON_5) - int(BFI_CON_9)
        print(con_score)
        neu_score = int(BFI_NEU_1) + int(BFI_NEU_3) + int(BFI_NEU_4) + int(BFI_NEU_8) + \
            int(BFI_NEU_6) + 12 - int(BFI_NEU_2) - \
            int(BFI_NEU_5) - int(BFI_NEU_7)
        print(neu_score)
        ope_score = int(BFI_OPEN_1) + int(BFI_OPEN_2) + int(BFI_OPEN_3) + int(BFI_OPEN_4) + int(BFI_OPEN_5) + \
            int(BFI_OPEN_6) + int(BFI_OPEN_8) + int(BFI_OPEN_10) + \
            8 - int(BFI_OPEN_7) - int(BFI_OPEN_9)
        print(ope_score)

        extra_norm = round(((extra_score - 14)/8)*8)
        print(extra_norm)
        arr.append(extra_norm)
        agre_norm = round(((agre_score - 17)/4)*8)
        print(agre_norm)
        arr.append(agre_norm)
        con_norm = round(((con_score - 17)/4)*8)
        print(con_norm)
        arr.append(con_norm)
        neu_norm = round(((neu_score - 14)/8)*8)
        print(neu_norm)
        arr.append(neu_norm)
        ope_norm = round(((ope_score - 14)/24)*8)
        print(ope_norm)
        arr.append(ope_norm)

        # print('Hello')
        # print(arr.shape)
        print(arr)
        # print(type(arr))
        # arr is input  data from form
        Prediction = loaded_model.predict([arr])
        personality = Prediction[0]  # class label predicted
        print(Prediction)

        ext_i = ""
        agre_i = ""
        con_i = ""
        neu_i = ""
        ope_i = ""

        if(extra_score >= 14 and extra_score < 17):
            ext_i = "Low Extraverteness"
        elif(extra_score >= 17 and extra_score < 20):
            ext_i = "Medium Extravertness"
        else:
            ext_i = "High Extravertness"

        if(agre_score >= 17 and agre_score <= 18):
            agre_i = "Low Agreeableness"
        elif(agre_score > 18 and agre_score <= 19):
            agre_i = "Medium Agreeableness"
        else:
            agre_i = "High Agreeableness"

        if(con_score >= 17 and con_score <= 18):
            con_i = "Low Conscientiousness"
        elif(con_score > 18 and con_score <= 19):
            con_i = "Medium Conscientiousness"
        else:
            con_i = "High Conscientiousness"

        if(neu_score >= 14 and neu_score < 17):
            neu_i = "Low Neuroticism"
        elif(neu_score >= 17 and neu_score < 20):
            neu_i = "Medium Neuroticism"
        else:
            neu_i = "High Neuroticism"

        if(ope_score >= 14 and ope_score < 22):
            ope_i = "Low Openess"
        elif(ope_score >= 22 and ope_score < 30):
            ope_i = "Medium Openess"
        else:
            ope_i = "High Openess"

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO history(id2, id,extravertness,agreeableness,conscientiousness ,neuroticism,openess,personality,test1 )  VALUES(NULL, % s, % s, % s, % s, % s, % s, % s, %s)', (session['id'] ,NULL ,NULL ,NULL ,NULL ,NULL ,NULL,0))
        mysql.connection.commit()
        cursor.execute('select id2 from history where id = %s and test1=0', (session['id'],))
        myresult = cursor.fetchone()
        hist_id = (myresult['id2'])


        
        cursor.execute('UPDATE history SET extravertness = % s WHERE id2 = % s;',(ext_i,hist_id ,  ))
        mysql.connection.commit()
        cursor.execute('UPDATE history SET agreeableness = % s WHERE id2 = % s;',(agre_i, hist_id ,  ))
        mysql.connection.commit()
        cursor.execute('UPDATE history SET conscientiousness = % s WHERE id2 = % s;',(con_i, hist_id ,  ))
        mysql.connection.commit()
        cursor.execute('UPDATE history SET neuroticism = % s WHERE id2 = % s;',(neu_i, hist_id ,  ))
        mysql.connection.commit()
        cursor.execute('UPDATE history SET openess = % s WHERE id2 = % s;',(ope_i, hist_id ,  ))
        mysql.connection.commit()
        cursor.execute('UPDATE history SET personality = % s WHERE id2 = % s;',(personality,hist_id , ))
        mysql.connection.commit()
        cursor.execute('UPDATE history SET test1 = 1 WHERE id2 = % s;',(hist_id , ))
        mysql.connection.commit()
        

        print(ext_i)
        print(agre_i)
        print(con_i)
        print(neu_i)
        print(ope_i)

        sum = "<h1 style='text-align:center'>Results</h1>"

        if(ext_i == "Low Extravertness"):
            sum = sum+"""
                <center><h4><u><b>You are low in extroversion - Introvert</b></u></h4></center>\n\n 
                If you scored low in extroversion, you’re more traditional label is “introvert”. Introverts get energy from alone time and like to recharge in solitude. This is you if you need lots of alone time before or after social events. You do not like loud, open parties or networking events and sometimes feel overwhelmed by talkative, outgoing extroverts (although they can be entertaining!) You are often not the most talkative person in the room, but when you do say something it is very meaningful.

                If you want to maximize your introversion, try:\n

                1. Finding the perfect recharge activities — sometimes watching TV isn’t enough. Try meditating, journaling or a creative outlet to nourish yourself.\n
                2. You do not have to pretend to be an extrovert to be charismatic — develop your own kind of charisma with a quiet presence.\n\n\n

                """

        if(ext_i == "Medium Extravertness"):
            sum = """
                <center><u><h4><b>You are Medium in extroversion - Ambivert</b></u></h4></center>\n\n
                Extroversion describes how you interact with people. People who are medium in extroversion are called ambiverts because they can dial up or dial down depending on the situation. You are very adaptable to people situations — if you need to be outgoing, you can be, but it is draining. You can also spend an entire day alone very happy and content — but three days in a row might be too many.

                If you want to maximize your ambiversion, try:\n

                1. Finding the people who make you your best self. Ambiverts come alive around supportive people.\n
                2. Saying no to the people and places that drain you. The wrong social outings can be a source of dread for an entire week–just say no!\n\n\n

                """

        if(ext_i == "High Extravertness"):
            sum = """
                <center><h4><u><b>You are High in extraversion - Extrovert</b></u></h4></center>\n\n
                If you are an extrovert you thrive around people. High extroverts get energy when they are around people and crave social time. Extroverts also like to process verbally or with others. If you have a bad day, you want to commiserate with others. If you have a good day, you want to celebrate with others. You are typically the life of the party or the most outgoing person in the room. 

                If you want to maximize your high extraversion, try:\n

                1. Use your exceptional people abilities to connect people who need to know each other.\n
                2. Level up your interpersonal intelligence by becoming a master of conversation — try to get everyone (including introverts) talking in the next group or meeting you are in.
                \n\n\n
                """
        if(agre_i == "Low Agreeableness"):
            sum = sum+"""<center><h4><u><b>You are Low in Agreeableness - Challenger</b></u></h4></center>\n\n
                Agreeableness dictates how you work with others. People who rate low in agreeableness are more analytical — some might even call you emotionless or detached. This is because you give more meaning to research, data and unbiased opinions. You prefer logic to emotions. You tend to be more skeptical, so compromise can be hard for you. 

                If you want to maximize your low agreeableness, try:\n

                1. Signing up for projects that require an analytical eye — leverage your ability to seek truth.\n
                2. Cooperation and empathy do not come as naturally to you. Level-up your team-building skills with research, which is a natural strength!\n
                3. Partner with an empathetic colleague or friend to give you the inside look into behavior and communication when you need to get a team working together.\n\n\n

                """

        if(agre_i == "Medium Agreeeableness"):
            sum = sum+""" <center><h4><u><b>You are Medium in Agreeableness </u></h4></center>\n\n
                Agreeableness is how you feel toward others. If you are medium in agreeableness you are good at working with people — up until a point. Certain people drive you up the wall, but you can deal with them as long as you have a solid base of things you enjoy doing. You can work well on a team, but also thrive on solo projects.

                If you want to maximize your medium agreeableness, try:\n

                1. You can do it all — so you have to figure out what you truly want.\n
                2. Don’t say yes to toxic people or events you dread. Sometimes you have to stand up for yourself.\n
                3.Level up your team skills by learning to decode emotions. You already have a knack for this, but learning the science will make it even better.\n\n\n
                """

        if(agre_i == "High Agreeableness"):
            sum = sum+"""<center><h4><u><b>You are High in Agreeableness - Adapter</b></u></h4></center>\n\n 
                Highly agreeable people are “yes” people. If this is you then you like to say yes to every request. You may even be a people pleaser. If you rate high in agreeableness you are likely friendly and compassionate. Highly agreeable people are also typically great team players. You are likely empathetic and very good at getting people to collaborate and cooperate. You might also be good at getting people to feel at ease, which makes it so people like to open up to you (and tell you their life story!)

                If you want to maximize your high agreeableness, try:\n

                1. Do you struggle with being indecisive? This is because you want everyone else to be happy — make sure you are getting your needs met too.\n
                2. You are a great team player — and very good at supporting others and helping them. Leverage this super power!\n
                3. Learn your boundaries. If you are a people pleaser you can sometimes say yes to the wrong things.\n\n\n

                 """

        if(con_i == "Low Conscientiousness"):
            sum = sum+"""<center><h4><u><b>You are Low conscientious - Flexible</b></u></h4></center>\n\n 
                If you are low in conscientiousness you love to be flexible, unplanned and spontaneous. You would prefer to go with the flow as opposed to having a rigid plan. You tend to feel boxed in or limited by too many plans. Sometimes you can be late on projects or skip details, but you are very good at the big picture!

                If you want to maximize your low conscientiousness, try:\n

                1. Your flexibility makes you very spontaneous — lend this out to a friend who needs a break.\n
                2. Need to get organized considering hiring or partnering with someone who can do the details for you.\n
                3. Planners, apps and reminder technology will help manage details for you.\n\n\n
                    """

        if(con_i == "Medium Conscientiousness"):
            sum = sum+"""<center><h4><u><b>You are medium conscientiousness </b></u></h4></center>\n\n 
                Conscientiousness describes your approach to organization and details–which depends on your mood and the context. Sometimes you can be very organized and on top of things, but in the wrong situation or when you are overwhelmed, the details and deadlines slip. You know when you need to, you can dial up your effectiveness and get organized even though it is not your favorite skill.

                If you want to maximize your medium conscientiousness, try:\n

                1. Finding the people, places and situations that bring out the best of your abilities — those are the places where you thrive.\n
                2. Figure out your triggers for overwhelm and stress — and avoid them at all costs.\n
                3. Find a planner or organization app that fits with your aptitude for details.\n\n\n

                    """
        if(con_i == "High Conscientiousness"):
            sum = sum+"""<center><h4><u><b> You are High in Conscientiousness - Focused</b></u></h4></center>\n\n 
                Conscientiousness describes your approach to organization and details. If you are high in conscientiousness you are very organized. You love details and don’t like to be unplanned. You are efficient and excel at to do lists. You might especially enjoy checking things off your to do list for a job well done! You are dependable, dutiful and a hard worker. 

                If you want to maximize your high conscientiousness, try:\n

                1. Loaning out your organization abilities to a colleague or partner in need — what comes naturally to you does not come naturally to everyone else!\n
                2. Volunteering to be the coordinator, scheduler, note-taker at work or in your activities.\n
                3. Exercising your talent for detail with the right kinds of hobbies and projects.\n\n\n

                    """

        if(neu_i == "Low Neuroticism"):
            sum = sum+"""<center><h4><u><b>You are Low Neurotic - Resilinet</b></u></h4></center>\n\n 
                If you are low neurotic you are known for being stable and calm. You don’t have many mood swings or intense mood changes. You are not a worrier. This makes you a great laid-back partner and friend. You do not micromanage because you have faith that things will get done. You often see the best in people. 

                If you want to maximize your neuroticism, try:\n

                1. Adopting a high neurotic. Sometimes we need a little help.\n
                2. Leveraging your stability by joining a high pressure job or hobby (volunteer firefighting perhaps?). Your ability to stay calm in intense situations is rare!\n
                3. Have patience for emotional people in your life. Sometimes it is hard to understand the worriers in your life — but have compassion for them as they are not wired the same as you!\n\n\n
                """

        if(neu_i == "Medium Neuroticism"):
            sum = sum+""" <center><h4><u><b>You are Medium in Neuroticism. </b></u></h4></center>\n\n
                If you are medium in neuroticism, certain situations (or people) can set you off. You can get burned out if you sign up for too much. On a bad week, it is hard to fall asleep because you are worrying about all areas of your life. The good news is as a medium neurotic you can usually find ways to stabilize.

                     If you want to maximize your neuroticism, try:\n

                1. Noticing your anxiety triggers. What turns a neutral week into a bad week? Stop the triggers before they start.\n
                2. Creating some self-care routines to prevent burnout from happening in the first place.\n
                3. Find low neurotic friends to keep you grounded.\n\n\n
                    """

        if(neu_i == "High Neuroticism"):
            sum = sum+"""<center><h4><u><b>You are High in Neuroticism - Reactive</b></u></h4></center>\n\n
                 Neuroticism dictates how you approach worry. High neurotics are worriers. If you are high neurotic you tend to be more anxious. You might have more reaction when things do go wrong and it takes you a longer time to calm down. You also like to think through all kinds of options before making a decision. 

                If you want to maximize your high neuroticism, try:\n

                1. Doing more pros and cons lists — this thinking can take down anxiety.\n
                2. Partner with a low neurotic — they can be your calming, stable presence to keep you grounded.\n
                3.Find rituals that keep you calm. Can you try meditation or breathing techniques to cope with anxiety?\n\n\n
                    """

        if(ope_i == "Low Openess"):
            sum = sum+"""<center><h4><u><b>You are low open  - Preserver.</b></u></h4></center>\n\n
                If you are low in openness you love routine, rituals and habits. You love having lots of routines in your life and get excited for regular traditions. Predictability makes you feel comfortable and secure. You like to have control over your environment, schedule and life.

                If you want to maximize your low openness, try:\n

                1. Honor your love of ritual and build some feel-good habits into your life.\n
                2. Heading up a tradition in your office, family or life — be the holiday keeper of traditions.\n
                3. Let people in your life know that you do not like to be surprised by new things or routines.\n\n\n
                """
        if(ope_i == "Medium Openess"):
            sum = sum+"""<center><h4><u><b>You are medium Open</b></u></h4></center> \n\n
                If you are medium in openness you like to try new things when you are in the mood. With the right planning you enjoy a new experience, but you also love a good routine. You like to balance your schedule with a few new activities and people and habits you can depend on. You love balance.

                    If you want to maximize your medium openness, try:\n

                    1. Picking one new thing to try a month to spark creativity.\n
                    2. Honor one important ritual in your life by building a feel good habit.\n
                    3. Think of the 5 people you are closest to, who is your adventure buddy? Who is your homebody buddy?\n\n\n
                    """
        if(ope_i == "High Openess"):
            sum = sum+"""<center><h4><u><b>You are High in Open - Explorer</b></u></h4></center>\n\n
                If you are high in openness you love trying new things and having new experiences. You are curious and imaginative. You love coming up with new ideas and new ways of doing things. You thrive off of new! High opens often adventure and are usually the first to try something for the first time.

                    If you want to maximize your high openness, try:\n\

                    1. Signing up for a new activity every month — it will help you prevent burnout.\n
                    2. Exercising your imagination and talent for coming up with new ideas at work or with hobbies.\n
                    3. Finding an adventure buddy to help you exercise your high openness.\n\n\n
                    """

        if(Prediction[0] == 'extraverted'):
            sum = sum + """\n\n\n<h1><center><u><b><i>Personality Predicted is: Extraverted. </h1></center></u></b></i>\n\n\n<center><h3>Here are some of the recommended songs to mellow down the energy:\n
                <div class="container">
                1. Only Time\n
                2. Chahun Main Ya Na\n
                3. Tum Ho\n
                4. Saajna Unplugged\n
                5. Rehna Tu</center></h3>\n
                \n  
                </div>
                """
        if(Prediction[0] == 'serious'):
            sum = sum+"""\n\n\n<h1><center><u><b><i>Personality Predicted is : Serious.  </h1></center></u></b></i>\n\n\n<center><h3>Here are some recommended songs to liven up the energy:\n
                <div class="container">
                1. The Bussiness\n
                2. Bananza\n
                3. Dance Monkey\n
                4. Freed from Desire\n
                5. Gimme Gimme Gimme\n</center></h3>
                </div>
                """

        if(Prediction[0] == 'responsible'):
            sum = sum+"""\n\n\n <h1 ><center></u></b></i>Personality Predicted is : Responsible. </h1></center></u></b></i>\n\n\n <center><h3>Here are some recommended songs :)\n
              <div class="container">
                1. Dil KO Karaar\n
                2. Ranjha\n
                3. Tu Aake Dekhle\n
                4. Aashiqui Aa Gayi\n
                5. Agar Tum Saath Ho\n</center></h3>
                </div>
                """

        if(Prediction[0] == 'lively'):
            sum = sum+"""\n\n\n <h1 ><center></u></b></i>Personality Predicted is : Lively.  </h1></center></u></b></i>\n\n\n<center><h3>Here are some recommended songs :\n
             <div class="container">
                1. Good Times\n
                2. The Best\n
                3. Respect\n
                4. Spinning Around\n
                5. We Are Family\n</center></h3>
                </div>
                """

        if(Prediction[0] == 'dependable'):
            sum = sum+"""\n\n\n <h1 ><center></u></b></i>Personality Predicted is : Dependable.  </h1></center></u></b></i>\n\n\n<center><h3>Here are somne recommended songs :\n
               <div class="container">
                1. Eye of the Tiger\n
                2. Stronger\n
                3. Lose Yourself\n
                4. Walking on Sunshine<br/>
                5. Remember the Name\n</center></h3>
                </div>
                """

        print(sum)
        text = sum.replace('\n', '<br>')
        print(text)
        return render_template('results.html', sum=Markup(text))

    else:
        return render_template('app.html')


if __name__ == "__main__":
    app.run(debug=True)
