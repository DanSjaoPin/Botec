from random import random


introductory_construction = ['- это',
                             'у нас',
                             'точно не',
                             'ааххаха',
                             '-',
                             'называется',
                             'тот еще',
                             'называется',
                             'его величество',
                             'пусть будет',
                             'называйте его так всегда -',
							 'похож на']

who_is_me_list = ['сияющий лаготворитель',
				  'лучезарный хрометей',
				  'полубокий однобок',
				  'пивви-бух',
				  'незабитый мяч',
				  'лоту кеды',
				  'поменявшийся каток лотку',
				  'лiдскае вкусное',
				  'ыизнерадостный душевноздоровый',
				  'карликовый дракон',
				  'осадный президент',
				  'преславутый пират',
				  'карликовый мяч',
                  'ворчливый Перфоратор',
				  'гондон',
				  'педрила тупорылый',
				  'усатый',
                  'дворовая скачелька',
				  'вышеупомянутый ниже-названный',
                  'властелин-пластилин',
				  'никто',
				  'бибка',
				  'бобка',
				  'Биба',
				  'Боба',
				  'Лупа',
                  'Пупа', 
				  'Залупа',
				  'и Бибка, и Бобка',
				  'жопа',
				  'щербатый',
				  'торч',
				  'членодевка',
				  'вверх, вниз и обратно',
				  'особо одаренный',
				  'индивидуум',
				  'гений',
				  'iq 20',
				  'ничесси',
                  'Хахладыж',
				  'Никита, прости его Г-споди...',
				  'ПЕРЕПИЗДРЮЧЕННЫЙ ГОЛШТИНСКИЙ ПИЗДОДЕРЖЕЦ',
                  'ХУЯЛЫГА ПИЗДОДРАЧЕНАЯ',
                  'смердящий скунс',
				  'шкила',
				  'Z',
				  'зубной состав',
				  'оргазм насвая',
                  'талантливый бесталантище',
                  'иситчик на хую виситчик',
				  'говно залупа пенис хер',
                  'краткий утëнок', 
				  'подзалупный творожок',
				  'удав в кулаке',
				  'одноглазый змей',
				  'зверь с тремя ликами',
				  'EVA 00',
                  'EVA 01',
				  'EVA 02',
				  'ded',
				  'желчестрадающий ангел',
				  'убуб',
				  'вагнеровец с кувалдой',
				  'установленная винда',
                  'генетическая помарка', 
				  'дристающий ангел',
				  'взрыв кабачка в коляске с поносом',
				  'синдромирующий живым труп',
				  'демон из зада',
				  'расщепленный неделимый',
                  'монолитный стихотворец',
                  'клаксующий такосон',
                  'колющийся ёж',
                  'полоска на еноте',
                  'число авангарда',
                  'блевотина распутного бомжа',
                  'веревка без мыла',
                  'табуретка с четырмя людьми на ножках',
                  'Виталя',
                  'абсолютный Никита', 
				  '3D: дебил, дурак и долбаеб', 
				  'рассчитаный однораз',
				  'заяц из пениса',
				  'вибратор',
				  'растущий гемоглабин',
                  'зубная вош', 
				  'пубертатная язва',
				  'педрила-гомодрила',
				  'ганзолька',
                  'волосатый боребух',
                  'отчисленец',
                  'неуродимая медицина',
                  'Алиноподобное сцущество',
                  'сектор "ДРИСЬ"',
                  'распространитель тронов',
                  'коричневый алабай',
                  'жмышевский бурят',
                  'чередование знаков',
                  'драгоценный щебень',
                  'овощной опус', 
                  'голубой слон',
                  'зеленый слоник',
                  'черствый Олег',
                  'червивая матка',
                  'портированный DOOM',
                  'Зеленский',
                  'сгоревший ареал',
                  'страдающий дед',
                  'скаут',
                  'пиро', 
				  'солда',
				  'демоман',
				  'хеви',
				  'инженер',
				  'врач',
				  'снайпер',
				  'шпион',
				  'негр',
				  'раб на плантации',
				  'разбитое сердце',
				  'жопотрах',
				  'членосос',
				  'хуец',
				  'раздолбленный анус',
				  'сглыпа',
				  'Ярик',
				  'протекший бочок',
				  'тактильный человек',
				  'Кайл',
				  'Кенни',
				  'Стен',
				  'Картман',
				  'Вовка',
				  'круглый идиот',
				  'лямбда выражение',
				  'агонизирующий предлог',
				  'зубодробильный кусок',
				  'хозяйственное состояние',
				  'обделенный всем',
				  'опухоль в виде мозга',
				  'спам на почте',
				  'разделитель зада пополам',
				  'небинарный бинарный',
				  'трапик',
				  'сломанная газель',
				  'сортирный крикун',
				  'друг бактерий',
				  'злодей британец',
				  'недопонятый гений',
				  'ге(ни)й',
				  'бронхиальный СПИД',
				  'папка Люка',
				  'попугай Кеша',
				  'кiшка',
				  'коловритный модник',
				  'водный курсач',
				  'член членства многочленов',
				  'ты, просто ты',
				  'всенемогущее могущество',
				  'всемогущее немогущество',
				  'глина',
				  'ножной амбидекстер',
				  'трахтор',
				  'сексоратор',
				  'анальный дробитель',
				  'анальный грабитель',
				  'калловая масса непризнанного деда',
				  'барманьяк',
				  'скоковпитывалка',
				  'болотный жабомет',
				  'чернобыльский болтометатель',
				  'псевдонегр',
				  'Парамаунт Дикчерс',
				  'титановый хер',
				  'крылечко с колечка',
				  'анальный уничтожитель',
				  'смотритель прямой кишки',
				  'глиномес',
				  'многострадалец',
				  'смертный таракан',
				  'главграч',
				  'Неизвестный Исполнитель',
				  '1234567890',
				  'первый в списке пидоров',
				  'первопроходец уретры',
				  'уретральный глист',
				  'яйцо карлика',
				  'игровая простата',
				  'игривая девочка',
				  'отбитый и израненный',
                  'отпятное сцыкло',
                  'незаписанный файл',
                  'питонист',
                  'разбитый и недотраханный',
                  'главный злодей',
                  'зубастый немой',
                  'переломленный пополам разбитка',
                  'бургулированный артемид',
                  'гельминтозозависимый недосып',
                  'ургально-ванильный ираник']