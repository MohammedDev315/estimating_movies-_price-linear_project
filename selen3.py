from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from bs4 import BeautifulSoup
import requests
import time, os




options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


csv_file = open("result2.csv" , "a")
write_to_csv = csv.writer(csv_file)
write_to_csv.writerow([
                        'filem_name' ,
                        'tomatometerscore',
                        'audiencescore',
                        'reviews_numb',
                        'ratings_numb',
                       'rating' ,
                       'genre' ,
                       'language' ,
                       'director',
                       'producer',
                       'writer',
                       'release_date_theaters',
                       'release_date_streaming',
                       'box_office',
                       'runtime',
                       'distributor',
                       'aspect_ratio',
                        'actors'
                       ])


def get_move_data(move_name):
    driver.get("https://www.rottentomatoes.com")
    tem_dic = {}
    tem_dic['filem_name'] = move_name
    try:
        search = driver.find_element( By.XPATH , '//*[@id="navbar"]/search-algolia/search-algolia-controls/input')
        search.send_keys(move_name)
        search.send_keys(Keys.RETURN)

        try:
            ele2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, move_name))
            )
            ele2.click()
        except:
            print(f"Select By Name Not found ::  {move_name}")

        try:
            ele1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mainColumn"]/section[3]/div/div/ul/li[1]/div[2]' ))
            )
            show_more_actors_link = driver.find_element(By.XPATH , '//*[@id="showMoreCastAndCrew"]' )
            show_more_actors_link.click()

            scores = driver.find_element(By.XPATH, '//*[@id="topSection"]/div[1]/score-board')
            Reviews = driver.find_element(By.XPATH, '//*[@id="topSection"]/div[1]/score-board/a[1]').text
            Ratings = driver.find_element(By.XPATH, '//*[@id="topSection"]/div[1]/score-board/a[2]').text
            tem_dic['tomatometerscore'] = scores.get_attribute('tomatometerscore')
            tem_dic['audiencescore'] = scores.get_attribute('audiencescore')
            tem_dic['reviews_numb'] = int(Reviews.split()[0])
            tem_dic['ratings_numb'] = Ratings.split()[0]


            try:
                for li_num in range(1,14):
                    key_of_data = driver.find_element(By.XPATH , f'//*[@id="mainColumn"]/section[3]/div/div/ul/li[{li_num}]/div[1]' )
                    value_of_dat = driver.find_element(By.XPATH , f'//*[@id="mainColumn"]/section[3]/div/div/ul/li[{li_num}]/div[2]' )
                    print(f'Key : {key_of_data.text} --- Value = {value_of_dat.text} ')
                    tem_dic[key_of_data.text.replace(':', '')] = value_of_dat.text
            except:
                print(f"No more data are available -- {move_name}")

            try:
                all_actors_in_text = ''
                for div_num in range(1,11):
                    actor_name = driver.find_element(By.XPATH , f'//*[@id="movie-cast"]/div/div/div[{div_num}]/div[2]/a')
                    all_actors_in_text += actor_name.text
                    all_actors_in_text += ','
                tem_dic['actors'] = all_actors_in_text
                print(all_actors_in_text)
            except:
                print(f"No more Actors are available {move_name} ")
        except:
            print(f"No Data for : {move_name}")
    except :
        print(f"I can not find {move_name} at search ")
    print(tem_dic)
    #----------------------
    #Check each element
    if 'filem_name' not in tem_dic.keys() :  tem_dic['filem_name'] = None
    if 'tomatometerscore' not in tem_dic.keys() :  tem_dic['tomatometerscore'] = None
    if 'audiencescore' not in tem_dic.keys() :  tem_dic['audiencescore'] = None
    if 'reviews_numb' not in tem_dic.keys() :  tem_dic['reviews_numb'] = None
    if 'ratings_numb' not in tem_dic.keys() :  tem_dic['ratings_numb'] = None
    if 'Rating' not in tem_dic.keys() :  tem_dic['Rating'] = None
    if 'Genre' not in tem_dic.keys() :  tem_dic['Genre'] = None
    if 'Original Language' not in tem_dic.keys() :  tem_dic['Original Language'] = None
    if 'Director' not in tem_dic.keys() :  tem_dic['Director'] = None
    if 'Producer' not in tem_dic.keys() :  tem_dic['Producer'] = None
    if 'Writer' not in tem_dic.keys() :  tem_dic['Writer'] = None
    if 'Release Date (Theaters)' not in tem_dic.keys() :  tem_dic['Release Date (Theaters)'] = None
    if 'Release Date (Streaming)' not in tem_dic.keys() :  tem_dic['Release Date (Streaming)'] = None
    if 'Box Office (Gross USA)' not in tem_dic.keys() :  tem_dic['Box Office (Gross USA)'] = None
    if 'Runtime' not in tem_dic.keys() :  tem_dic['Runtime'] = None
    if 'Distributor' not in tem_dic.keys() :  tem_dic['Distributor'] = None
    if 'aspect_ratio' not in tem_dic.keys() :  tem_dic['aspect_ratio'] = None
    if 'actors' not in tem_dic.keys() :  tem_dic['actors'] = None
    #----------------------
    #Write to csv
    write_to_csv.writerow([
        tem_dic['filem_name'],
        tem_dic['tomatometerscore'],
        tem_dic['audiencescore'],
        tem_dic['reviews_numb'],
        tem_dic['ratings_numb'],
        tem_dic['Rating'],
        tem_dic['Genre'],
        tem_dic['Original Language'],
        tem_dic['Director'],
        tem_dic['Producer'],
        tem_dic['Writer'],
        tem_dic['Release Date (Theaters)'],
        tem_dic['Release Date (Streaming)'],
        tem_dic['Box Office (Gross USA)'],
        tem_dic['Runtime'],
        tem_dic['Distributor'],
        tem_dic['aspect_ratio'],
        tem_dic['actors']
    ])





move_names1 = ['Insidious: The Last Key', 'The Strange Ones', 'Stratton',
              'Sweet Country', 'The Commuter', 'Proud Mary', 'Acts of Violence',
              'Freak Show', 'Humor Me', 'Vazante', "Mary and the Witch's Flower",
              '12 Strong', 'Den of Thieves', 'Forever My Girl',
              'Maze Runner: The Death Cure', 'The Insult', 'Please Stand By',
              'Winchester', 'A Fantastic Woman', 'Armed', 'The Cloverfield Paradox',
              'Bad Apples', 'Peter Rabbit', 'Fifty Shades Freed', 'The 15:17 to Paris',
              'Lionsgate', 'Kri', 'Permission', 'Monster Family', 'Golden Exits',
              'Black Panther', 'Early Man', 'Loveless', 'The Party', 'Nostalgia',
              "Black '47", 'Samson', 'Game Night', 'Annihilation', 'Every Day', 'The Cured',
              'The Lodgers', 'Red Sparrow', 'Death Wish', 'The Vanishing of Sidney Hall',
              'Foxtrot', 'Pickings', 'A Wrinkle in Time', 'Gringo', 'Thoroughbreds',
              'The Death of Stalin', 'The Leisure Seeker', 'The Strangers: Prey at Night',
              'The Hurricane Heist', 'Tomb Raider', 'Love, Simon', 'I Can Only Imagine',
              '7 Days in Entebbe', 'Furlough', 'Josie', 'Flower', 'Pacific Rim: Uprising',
              'Isle of Dogs', 'Sherlock Gnomes', 'Unsane', 'Paul, Apostle of Christ',
              'Final Portrait', 'Midnight Sun', '[70]', 'Ready Player One',
              "Tyler Perry's Acrimony", "God's Not Dead: A Light in Darkness", 'Gemini',
              'The Last Movie Star', 'A Quiet Place', 'Blockers', 'You Were Never Really Here',
              'Chappaquiddick', 'Warner Bros. Pictures', 'Lean on Pete', 'The Miracle Season',
              'Beirut', 'Rampage', 'Truth or Dare', 'The Rider', 'Sgt. Stubby: An American Hero',
              'I Feel Pretty', 'Super Troopers 2', 'Traffik', 'The House of Tomorrow',
              'Liz and the Blue Bird', 'Avengers: Infinity War', 'Disobedience',
              'Backstabbing for Beginners', 'Kings', 'Overboard', 'Tully', 'Bad Samaritan',
              'The Cleanse', 'The Guardians']


move_names2 = ['Breaking In', 'The Seagull', 'Terminal', 'Revenge', 'Deadpool 2', 'Book Club', 'First Reformed', 'Pope Francis: A Man of His Word', 'Show Dogs', 'Solo: A Star Wars Story', 'How to Talk to Girls at Parties', 'In Darkness', 'The Misandrists', 'Future World', 'Action Point', 'Adrift', 'Upgrade', 'American Animals', 'Social Animals', "Ocean's 8", "Won't You Be My Neighbor?", 'Hereditary', 'Hotel Artemis', 'Superfly', 'Incredibles 2', 'Tag', 'On Chesil Beach', 'Gotti', 'Jurassic World: Fallen Kingdom', 'Boundaries', 'Damsel', 'The Domestics', 'Sicario: Day of the Soldado', 'Leave No Trace', 'Uncle Drew', 'Woman Walks Ahead', 'The First Purge', 'Ant-Man and the Wasp', 'Sorry to Bother You', 'Whitney', 'Hotel Transylvania 3: Summer Vacation', 'Skyscraper', 'Eighth Grade', "Don't Worry, He Won't Get Far on Foot", 'Shock and Awe', 'Mamma Mia! Here We Go Again', 'The Equalizer 2', 'Blindspotting', 'Unfriended: Dark Web', 'Bleach', 'Cohen Media Group', 'Mission: Impossible – Fallout', 'Teen Titans Go! To the Movies', 'Detective Dee: The Four Heavenly Kings', 'Hot Summer Nights', 'Puzzle', 'Christopher Robin', 'The Darkest Minds', 'The Spy Who Dumped Me', 'The Miseducation of Cameron Post', "Never Goin' Back", 'Dog Days', 'The Meg', 'BlacKkKlansman', 'Slender Man', 'A Prayer Before Dawn', 'Crazy Rich Asians', 'Alpha', 'Mile 22', 'The Wife', 'Billionaire Boys Club', 'Juliet, Naked', 'Down a Dark Hall', "To All the Boys I've Loved Before", 'The Happytime Murders', 'Searching', 'Papillon', 'A.X.L.', 'Operation Finale', 'Kin', 'The Little Stranger', 'Destination Wedding', 'The Nun', 'Peppermint', 'The Predator', 'White Boy Rick', 'A Simple Favor', 'The Children Act', 'Lizzie', 'Unbroken: Path to Redemption', 'Hell House LLC II: The Abaddon Hotel', 'The House with a Clock in Its Walls', 'Life Itself', 'The Sisters Brothers', 'Assassination Nation', 'Colette', 'Fahrenheit 11/9', 'Christian Carion', 'Love, Gilda', 'My Hero Academia: Two Heroes', 'Smallfoot', 'Night School', 'The Old Man & the Gun', 'Hell Fest', 'Five & Two Pictures', 'Venom', 'A Star Is Born', 'The Hate U Give', 'The Happy Prince', 'First Man', 'Bad Times at the El Royale', 'Goosebumps 2: Haunted Halloween', 'Beautiful Boy', 'The Oath', "Gosnell: The Trial of America's Biggest Serial Killer", 'After Everything', 'Halloween', 'Can You Ever Forgive Me?', 'Mid90s', 'Wildlife', 'What They Had', 'Hunter Killer', 'Johnny English Strikes Again', 'Suspiria', 'Indivisible', 'Bullitt County', 'Bohemian Rhapsody', 'The Nutcracker and the Four Realms', "Nobody's Fool", 'Boy Erased', 'A Private War', 'Bodied', 'The Front Runner', 'The Grinch', "The Girl in the Spider's Web", 'Overlord', 'The Ballad of Buster Scruggs', 'Lazer Team 2', 'Lionsgate', 'Fantastic Beasts: The Crimes of Grindelwald', 'Widows', 'Instant Family', 'Ralph Breaks the Internet', 'Creed II', 'Green Book', 'Robin Hood', 'Roma', 'The Favourite', 'Mowgli: Legend of the Jungle', 'The Possession of Hannah Grace', 'Anna and the Apocalypse', 'Capernaum', 'Mary Queen of Scots', 'Ben Is Back', 'Spider-Man: Into the Spider-Verse']

move_names3 = ['Escape Room', 'Rust Creek', 'American Hangman', "A Dog's Way Home", 'The Upside', 'Replicas', 'After Darkness', 'Glass', 'Close', 'The Standoff at Sparrow Creek', 'The Final Wish', 'The Kid Who Would Be King', 'Serenity', 'I Am Mother', 'The Vast of Night', 'Miss Bala', 'Velvet Buzzsaw', 'Piercing', 'The Lego Movie 2: The Second Part', 'What Men Want', 'Cold Pursuit', 'High Flying Bird', 'The Prodigy', "Isn't It Romantic", 'Happy Death Day 2U', 'Alita: Battle Angel', 'How to Train Your Dragon: The Hidden World', 'Fighting with My Family', "Tyler Perry's A Madea Family Funeral", 'Greta', 'Triple Frontier', 'Captain Marvel', 'The Kid', 'Wonder Park', 'Captive State', 'Nancy Drew and the Hidden Staircase', 'The Aftermath', 'Five Feet Apart', 'The Highwaymen', 'Red 11', 'Never Grow Old', 'Triple Threat', 'Us', 'Hotel Mumbai', 'The Dirt', 'Dragged Across Concrete', 'Dumbo', 'The Beach Bum', 'Unplanned', 'Shazam!', 'Pet Sematary', 'The Best of Enemies', 'High Life', 'Unicorn Store', 'The Haunting of Sharon Tate', 'The Wind', 'The Silence', 'Hellboy', 'Little', 'Missing Link', 'After', 'Her Smell', 'Breakthrough', 'Penguins', 'The Curse of La Llorona', 'Under the Silver Lake', 'Family', 'Fast Color', 'Someone Great', 'I Spit on Your Grave: Deja Vu', 'Avengers: Endgame', 'I Trapped the Devil', 'Body at Brighton Rock', 'Buffaloed', 'Long Shot', 'The Intruder', 'UglyDolls', 'Extremely Wicked, Shockingly Evil and Vile', 'The Last Summer', 'Pokémon Detective Pikachu', 'The Hustle', 'Tolkien', 'Poms', 'The Professor and the Madman', 'John Wick: Chapter 3 – Parabellum', "A Dog's Journey", 'The Sun Is Also a Star', 'The Professor', 'The Souvenir', 'The Tomorrow Man', 'Aladdin', 'Brightburn', 'Booksmart', 'The Perfection', 'Always Be My Maybe', 'Godzilla: King of the Monsters', 'Rocketman', 'Ma', 'Dark Phoenix', 'The Secret Life of Pets 2', 'Late Night', 'The Last Black Man in San Francisco', 'Changeland', 'Men in Black: International', 'Shaft', "The Dead Don't Die", 'Murder Mystery', 'Plus One', 'Being Frank', 'Toy Story 4', 'Anna', "Child's Play", 'Annabelle Comes Home', 'Yesterday', 'Ophelia', 'Killers Anonymous', 'Spider-Man: Far From Home', 'Escape Plan: The Extractors', 'Midsommar', 'Stuber', 'Crawl', 'Point Blank', 'The Farewell', "Darlin'", 'The Lion King', 'Once Upon a Time in Hollywood', 'Skin', 'The Red Sea Diving Resort', 'Fast & Furious Presents: Hobbs & Shaw', 'A Score to Settle', 'The Operative', 'Dora and the Lost City of Gold', 'The Kitchen', 'The Art of Racing in the Rain', 'Scary Stories to Tell in the Dark', 'The Peanut Butter Falcon', 'After the Wedding', 'Light of My Life', 'The Angry Birds Movie 2', 'Good Boys', 'Blinded by the Light', "Where'd You Go, Bernadette", '47 Meters Down: Uncaged', 'Gwen', 'Ready or Not', 'Angel Has Fallen', 'Brittany Runs a Marathon', 'Overcomer', "Jacob's Ladder", 'Burn', 'Official Secrets', "Don't Let Go", 'Itsy Bitsy', 'The Fanatic', 'It Chapter Two', 'Satanic Panic', 'The Obituary of Tunde Johnson', 'The Goldfinch', 'Hustlers', 'The Sound of Silence', 'Monos', 'Tall Girl', 'Polaroid', 'Ad Astra', 'Downton Abbey', 'Rambo: Last Blood', 'Bloodline', 'Running with the Devil', 'Fractured', 'Abominable', 'The Laundromat', 'Judy', 'Prey', 'Joker', 'Lucy in the Sky', 'Dolemite Is My Name', 'In the Tall Grass', 'Low Tide', 'Wrinkles the Clown', 'Little Monsters', 'Gemini Man', 'The Addams Family', 'The King', 'Jexi', 'El Camino: A Breaking Bad Movie', 'Maleficent: Mistress of Evil', 'Zombieland: Double Tap', 'Jojo Rabbit', 'The Lighthouse', 'Wounds', 'Black and Blue', 'The Current War', 'Countdown', 'The Kill Team', 'The Gallows Act II', 'Terminator: Dark Fate', 'Motherless Brooklyn', 'The Irishman', 'Harriet', 'Arctic Dogs', 'Marriage Story', 'Doctor Sleep', 'Last Christmas', 'Playing with Fire', 'Let It Snow', 'Midway', 'Klaus', 'Honey Boy', 'Lady and the Tramp', 'Noelle', 'Ford v Ferrari', "Charlie's Angels", 'The Good Liar', 'The Report', 'Waves', 'Frozen II', 'A Beautiful Day in the Neighborhood', '21 Bridges', 'Dark Waters', 'Knives Out', 'Queen & Slim', 'The Two Popes', 'Playmobil: The Movie', 'The Aeronauts', 'A Million Little Pieces', "Daniel Isn't Real", 'Jumanji: The Next Level', 'Richard Jewell', 'Black Christmas', '6 Underground', 'Bombshell', 'Uncut Gems', 'Seberg', 'A Hidden Life', 'Star Wars: The Rise of Skywalker', 'Cats', 'Togo', 'Spies in Disguise', 'Little Women', '1917', 'Just Mercy', 'Clemency']

move_names2017 = ['Underworld: Blood Wars', 'Arsenal', 'Between Us', 'Monster Trucks', 'The Bye Bye Man', 'Sleepless', '100 Streets', 'The Book of Love', 'Split', 'XXX: Return of Xander Cage', 'The Resurrection of Gavin Stone', 'Trespass Against Us', 'Sophie and the Rising Sun', "A Dog's Purpose", 'Resident Evil: The Final Chapter', 'Lost in Florence', 'I Am Michael', 'iBoy', 'Rings', 'The Space Between Us', 'Youth in Oregon', 'I Am Not Your Negro', 'Growing Up Smith', 'The Lego Batman Movie', 'Fifty Shades Darker', 'John Wick: Chapter 2', 'Michael Johnston', 'The Great Wall', 'A Cure for Wellness', 'Fist Fight', 'American Fable', 'XX', 'Lovesong', 'Get Out', 'Rock Dog', 'Collide', 'The Girl with All the Gifts', "I Don't Feel at Home in This World Anymore", 'Logan', 'The Shack', 'Before I Fall', 'Table 19', 'The Last Word', 'Catfight', 'Donald Cried', 'Kong: Skull Island', 'Burning Sands', 'Beauty and the Beast', 'The Belko Experiment', 'Song to Song', 'Atomica', 'All Nighter', "The Devil's Candy", 'Power Rangers', 'Life', 'CHiPs', 'Wilson', 'Brandon Dickerson', 'Car Dogs', 'Scott Eastwood', 'The Marine 5: Battleground', 'Ghost in the Shell', 'The Boss Baby', "The Zookeeper's Wife", "The Blackcoat's Daughter", 'The Discovery', 'Carrie Pilby', 'The Case for Christ', 'Smurfs: The Lost Village', 'Going in Style', 'Colossal', 'Gifted', 'Aftermath', 'The Fate of the Furious', 'Spark', 'The Lost City of Z', 'My Entire High School Sinking Into the Sea', 'The Outcasts', 'Born in China', 'Unforgettable', 'The Promise', 'The Circle', 'How to Be a Latin Lover', 'Sleight', 'Becoming Bond', 'Guardians of the Galaxy Vol. 2', 'The Lovers', '3 Generations', 'King Arthur: Legend of the Sword', 'Snatched', 'Lowriders', 'The Wall', 'Paris Can Wait', 'Alien: Covenant', 'Diary of a Wimpy Kid: The Long Haul', 'Everything, Everything', 'Wakefield', 'Baywatch', 'Pirates of the Caribbean: Dead Men Tell No Tales', 'Buena Vista Social Club: Adios', 'War Machine', 'Wonder Woman', 'Captain Underpants: The First Epic Movie', 'Dean', 'The Mummy', 'It Comes at Night', 'My Cousin Rachel', 'Megan Leavey', 'Beatriz at Dinner', 'Cars 3', 'Rough Night', 'All Eyez on Me', '47 Meters Down', 'The Book of Henry', 'Transformers: The Last Knight', 'The Beguiled', 'The Big Sick', 'The Bad Batch', 'Baby Driver', 'Okja', 'Despicable Me 3', 'The House', 'The Little Hours', 'Inconceivable', '2:22', 'A Ghost Story', 'Spider-Man: Homecoming', 'War for the Planet of the Apes', 'Wish Upon', 'Dunkirk', 'Girls Trip', 'First Kill', 'Atomic Blonde', 'The Emoji Movie', 'An Inconvenient Sequel: Truth to Power', 'Detroit', 'Brigsby Bear', 'Menashe', 'The Dark Tower', 'Kidnap', 'Step', 'Wind River', 'Armed Response', 'Annabelle: Creation', 'The Glass Castle', 'The Nut Job 2: Nutty by Nature', 'Good Time', 'Ingrid Goes West', 'The Only Living Boy in New York', "The Hitman's Bodyguard", 'Logan Lucky', 'Patti Cake$', 'Victor Crowley', 'All Saints', 'Entertainment Studios', 'Beach Rats', "Film Stars Don't Die in Liverpool", 'Tulip Fever', 'Unlocked', 'It', 'Home Again', '9/11', 'The Good Catholic', 'Gun Shy', 'Fallen', 'American Assassin', 'Mother!', "Brad's Status", 'Kingsman: The Golden Circle', 'The Lego Ninjago Movie', 'Stronger', 'Battle of the Sexes', 'Woodshock', 'Victoria & Abdul', '(Romance) in the Digital Age', 'Jeepers Creepers 3', 'American Made', 'Flatliners', 'Mark Felt: The Man Who Brought Down the White House', 'Blade Runner 2049', 'The Mountain Between Us', 'My Little Pony: The Movie', 'The Florida Project', 'Brawl in Cell Block 99', 'Happy Death Day', 'Marshall', 'Breathe', 'Goodbye Christopher Robin', 'Professor Marston and the Wonder Women', 'Blood Money', 'Geostorm', 'Only the Brave', 'Boo 2! A Madea Halloween', 'Same Kind of Different as Me', 'Leatherface', 'Wonderstruck', 'The Killing of a Sacred Deer', 'Thank You for Your Service', 'Suburbicon', 'Jigsaw', 'Novitiate', 'All I See Is You', 'Amityville: The Awakening', 'Thor: Ragnarok', 'A Bad Moms Christmas', 'Last Flag Flying', 'Lady Bird', 'Murder on the Orient Express', "Daddy's Home 2", 'LBJ', 'Three Billboards Outside Ebbing, Missouri', 'Mayhem', 'Justice League', 'The Star', 'Wonder', 'Cook Off!', 'Mr. Roosevelt', 'Roman J. Israel, Esq.', 'Coco', 'Darkest Hour', 'The Man Who Invented Christmas', 'Call Me by Your Name', 'The Disaster Artist', 'The Shape of Water', 'Wonder Wheel', 'I, Tonya', 'Just Getting Started', 'Star Wars: The Last Jedi', 'Ferdinand', 'Beyond Skyline', 'Jumanji: Welcome to the Jungle', 'The Greatest Showman', 'Pitch Perfect 3', 'Downsizing', 'Father Figures', 'The Post', 'Bright', 'Crooked House', 'Hostiles', 'All the Money in the World', "Molly's Game", 'Phantom Thread']

move_name2016 = ['The Forest', 'Anesthesia', 'Lamb', 'Ride Along 2', '13 Hours: The Secret Soldiers of Benghazi', 'Norm of the North', 'The Benefactor', 'Dirty Grandpa', 'The 5th Wave', 'The Boy', 'Synchronicity', 'Kung Fu Panda 3', 'The Finest Hours', 'Fifty Shades of Black', 'Jane Got a Gun', 'Hail, Caesar!', 'Pride + Prejudice + Zombies', 'The Choice', 'Deadpool', 'Zoolander 2', 'How to Be Single', 'Risen', 'The Witch', 'Race', 'Crouching Tiger, Hidden Dragon: Sword of Destiny', 'Gods of Egypt', 'Triple 9', 'Eddie the Eagle', 'Zootopia', 'London Has Fallen', 'Whiskey Tango Foxtrot', 'The Other Side of the Door', '10 Cloverfield Lane', 'The Young Messiah', 'The Perfect Match', 'Hello, My Name Is Doris', 'Miracles from Heaven', 'The Divergent Series: Allegiant', 'The Bronze', 'Midnight Special', 'Batman v Superman: Dawn of Justice', 'My Big Fat Greek Wedding 2', 'I Saw the Light', 'Everybody Wants Some!!', "God's Not Dead 2", 'Meet the Blacks', 'Miles Ahead', 'Pandemic', 'The Boss', 'Hardcore Henry', 'Demolition', 'The Invitation', 'Hush', 'The Jungle Book', 'Barbershop: The Next Cut', 'Criminal', 'Green Room', "The Huntsman: Winter's War", 'A Hologram for the King', 'Elvis & Nixon', 'Keanu', "Mother's Day", 'Ratchet & Clank', 'Captain America: Civil War', 'Money Monster', 'Sundown', 'The Darkness', 'Love & Friendship', 'The Angry Birds Movie', 'Neighbors 2: Sorority Rising', 'The Nice Guys', 'X-Men: Apocalypse', 'Alice Through the Looking Glass', 'Teenage Mutant Ninja Turtles: Out of the Shadows', 'Me Before You', 'Popstar: Never Stop Never Stopping', 'The Conjuring 2', 'Warcraft', 'Now You See Me 2', 'Finding Dory', 'Central Intelligence', 'Independence Day: Resurgence', 'The Shallows', 'Free State of Jones', 'The Neon Demon', 'The Legend of Tarzan', 'The BFG', 'The Purge: Election Year', 'The Secret Life of Pets', 'Captain Fantastic', 'Mike and Dave Need Wedding Dates', 'Characterz', 'The Infiltrator', 'Ghostbusters', 'Star Trek Beyond', 'Batman: The Killing Joke', 'Ice Age: Collision Course', 'Lights Out', 'Nerve', 'Jason Bourne', 'Bad Moms', 'Suicide Squad', 'Nine Lives', "Pete's Dragon", 'Sausage Party', 'Florence Foster Jenkins', 'Ben-Hur', 'Kubo and the Two Strings', 'War Dogs', 'Mechanic: Resurrection', "Don't Breathe", 'Hands of Stone', 'The Light Between Oceans', 'Morgan', 'Skiptrace', 'Sully', 'When the Bough Breaks', 'Robinson Crusoe', 'The Disappointments Room', "Bridget Jones's Baby", 'Snowden', 'Blair Witch', 'Hillsong: Let Hope Rise', 'The Magnificent Seven', 'Storks', "Miss Peregrine's Home for Peculiar Children", 'Deepwater Horizon', 'Queen of Katwe', 'Masterminds', 'The Girl on the Train', 'The Birth of a Nation', 'Middle School: The Worst Years of My Life', 'The Accountant', 'Kevin Hart: What Now?', 'Max Steel', 'Jack Reacher: Never Go Back', 'Keeping Up with the Joneses', 'Ouija: Origin of Evil', 'Boo! A Madea Halloween', "I'm Not Ashamed", 'American Pastoral', 'Inferno', 'Doctor Strange', 'Trolls', 'Hacksaw Ridge', 'Loving', 'The Love Witch', 'Arrival', "Billy Lynn's Long Halftime Walk", 'Almost Christmas', 'Shut In', 'Fantastic Beasts and Where to Find Them', 'The Edge of Seventeen', 'Bleed for This', 'Moana', 'Allied', 'Bad Santa 2', "Rules Don't Apply", 'La La Land', 'Rogue One: A Star Wars Story', 'The Founder', 'Sing', 'Patriots Day', 'A Monster Calls', 'Paterson']

move_name2015 = ['The Woman in Black: Angel of Death', 'Taken 3', "Let's Kill Ward's Wife", 'Match', 'Blackhat', 'Little Accidents', 'Paddington', 'Spare Parts', 'The Wedding Ringer', 'Vice', 'Veronika Decides to Die', 'The Boy Next Door', 'The Humbling', 'Mortdecai', 'Song One', 'Strange Magic', "We'll Never Have Paris", 'Black or White', 'The Loft', 'Project Almanac', 'Wild Card', '3 Nights in the Desert', 'Enter the Dangerous Mind', 'Jupiter Ascending', 'Love, Rosie', 'Seventh Son', 'The SpongeBob Movie: Sponge Out of Water', 'The Voices', 'Accidental Love', 'Da Sweet Blood of Jesus', 'Fifty Shades of Grey', 'Kingsman: The Secret Service', 'The Last Five Years', 'The DUFF', 'Hot Tub Time Machine 2', 'McFarland, USA', 'Everly', 'Focus', 'The Lazarus Effect', 'Maps to the Stars', 'Out of the Dark', 'Bad Asses on the Bayou', 'Chappie', 'Road Hard', 'The Second Best Exotic Marigold Hotel', 'Unfinished Business', 'Faults', 'Cinderella', 'The Cobbler', 'Cymbeline', 'Home Sweet Hell', 'It Follows', 'Muck', 'Run All Night', 'Danny Collins', 'The Divergent Series: Insurgent', 'Do You Believe?', 'The Gunman', 'Tracers', 'The Walking Deceased', 'Get Hard', 'Home', 'Serena', "While We're Young", 'Furious 7', 'Woman in Gold', 'Ex Machina', 'The Longest Ride', 'Lost River', '1915', 'Alex of Venice', 'Beyond the Reach', 'Child 44', 'Monkey Kingdom', 'Paul Blart: Mall Cop 2', 'The Road Within', 'True Story', 'Unfriended', 'Adult Beginners', 'Blackbird', 'Brotherly Love', 'Just Before I Go', 'Little Boy', 'The Age of Adaline', 'Avengers: Age of Ultron', 'Far from the Madding Crowd', 'The D Train', 'Hot Pursuit', 'Maggie', 'Mad Max: Fury Road', 'Pitch Perfect 2', "I'll See You in My Dreams", 'Poltergeist', 'Tomorrowland', 'Aloha', 'San Andreas', 'Barely Lethal', 'Heaven Knows What', 'Spy', 'Entourage', 'Insidious: Chapter 3', 'Love & Mercy', 'Jurassic World', 'Me and Earl and the Dying Girl', 'Dope', 'Inside Out', 'Max', 'Ted 2', 'Terminator Genisys', 'Magic Mike XXL', 'Amy', 'Minions', 'The Gallows', 'Self/Less', 'Tangerine', 'Boulevard', 'Strangerland', 'Ant-Man', 'Trainwreck', 'Irrational Man', 'Mr. Holmes', 'Pixels', 'Southpaw', 'Paper Towns', 'The Vatican Tapes', 'Vacation', 'Mission Impossible: Rogue Nation', 'The Gift', 'Ricki and the Flash', 'Straight Outta Compton', 'The Man from U.N.C.L.E.', "She's Funny That Way", 'No Escape', 'Hitman: Agent 47', 'Before We Go', 'The Visit', 'The Perfect Guy', 'Sleeping with Other People', 'Black Mass', 'Everest', 'Sicario', 'War Pigs', 'Hotel Transylvania 2', '99 Homes', 'The Intern', 'Stonewall', 'Mississippi Grind', 'The Walk', 'The Martian', 'Steve Jobs', 'Pan', 'Knock Knock', 'Beasts of No Nation', 'Bridge of Spies', 'Crimson Peak', 'Goosebumps', 'Room', 'Woodlawn', 'Truth', 'Experimenter', 'Rock the Kasbah', 'Paranormal Activity: The Ghost Dimension', 'Jem and the Holograms', 'The Last Witch Hunter', 'Suffragette', 'Bone Tomahawk', 'I Smile Back', 'Scouts Guide to the Zombie Apocalypse', 'Our Brand Is Crisis', 'Burnt', 'Brooklyn', 'Spectre', 'Spotlight', 'The Peanuts Movie', 'The 33', 'My All American', 'By The Sea', 'Carol', 'The Hunger Games: Mockingjay – Part 2', 'Creed', 'The Good Dinosaur', 'Victor Frankenstein', 'Krampus', 'In the Heart of the Sea', 'The Big Short', 'Star Wars: The Force Awakens', 'Concussion', "Daddy's Home", 'Joy', 'Point Break', 'The Hateful Eight', 'The Revenant']

# for x in move_name2015:
#     get_move_data(x)

csv_file.close()



