var state_arr = new Array("Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal");

var s_a = new Array();
s_a[0] = "";
s_a[1] = " Adoni | Ananthapuram | Bhimavaram	|Chilakaluripet	|Chittoor	|Dharmavaram	|Eluru	Eluru|	Gudivada	|Guntakal	|Guntur	|Hindupur	|Kadapa	|Kadiri	|Kakinada	|Kurnool	|Machilipatnam  |	Madanapalle	|Mangalagiri	|	Nandyal	|	Narasaraopet	|Nellore	|Ongole	|Proddatur	|Rajamahendravaram	|Srikakulam	|Tadepalligudem	|Tadipatri	|Tenali	|Tirupati	|Vijayawada	|Visakhapatnam	|Vizianagaram";
s_a[2] = "Anjaw |Changlang|Dibang Valley|East Kameng|	East Siang	|Kurung Kumey	|	Lohit	|Lower Dibang Valley	|	Lower Subansiri	|Papum Pare	|	Tawang	|Tirap|Upper Siang	|Upper Subansiri	|West Kameng	|West Siang";
s_a[3] = "Udalguri | Karimganj | Cachar | Kamrup | Kamrup Metro | Karbi Anglong | Kokrajhar | Golaghat | Goalpara | Chirang | Dibrugarh | Dima Hasao | Tinsukia	| Darrang | Dhubri | Dhemaji | Nagaon | Nalbari | Bongaigaon | Barpeta | Baksa | Morigaon | Jorhat | Lakhimpur | Sivasagar | sonitpur | Hailakandi ";
s_a[4] = "Arrah	|Aurangabad	| Bagaha	|Begusarai	|Bettiah	|Bhagalpur	|Bihar Sharif		|Buxar|Chhapra|Danapur	|	Darbhanga	|Dehri |	Gaya|Hajipur	|	Jamalpur|	Jehanabad|	Katihar	|	Kishanganj	|	Mehsi	East |	Motihari|	Munger	|	Muzaffarpur	|	Nawada	|	Patna		|Purnia|	Saharsa	|	Sasaram	|	Sitamarhi	|	Siwan    ";
s_a[5] = "Ambikapur|Bhilai|Bilaspur|Dhamtari|Durg|Jagdalpur|Raipur|Rajnandgaon";
s_a[6] = "Madgaon|Panaji";
s_a[7] = "Ahmadabad|Amreli|Bharuch|Bhavnagar|Bhu|Dwarka|Gandhinagar|Godhra|Jamnagar|Junagadh|Kandla|Khambhat|Kheda|Mahesana|Morbi|Nadiad|Navsari|Okha|Palanpur|Patan|Porbandar|Rajkot|Surat|Surendranagar|Valsad|Veraval";
s_a[8] = "|Ambala|Bhiwani|Chandigarh|Faridabad|Firozpur Jhirka|Gurugram|Hansi|Hisar|Jind|Kaithal|Karnal|Kurukshetra|Panipat|Pehowa|Rewari|Rohtak|Sirsa|Sonipat";
s_a[9] = "|Bilaspur|Chamba|Dalhousie|Dharmshala|Hamirpur|Kangra|Kullu|Mandi|Nahan|Shimla|Una";
s_a[10] = "|Bokaro|Chaibasa|Deoghar|Dhanbad|Dumka|Giridih|Hazaribag|Jamshedpur|Jharia|Rajmahal|Ranchi|Saraikela";
s_a[11] = "Badami|Ballari|Bengaluru|Belagavi|Bhadravati|Bidar|Chikkamagaluru|Chitradurga|Davangere|Halebid|Hassan|Hubballi-Dharwad|Kalaburagi|Kolar|Madikeri|Mandya|Mangaluru|Mysuru|Raichur|Shivamogga|Shravanabelagola|Shrirangapattana|Tumakuru|Vijayapura";
s_a[12] = "Alappuzha|Vatakara|Idukk|Kannu|Koch|Kolla|Kottaya|Kozhikod|Mattancher|Palakka|Thalasser|Thiruvananthapura|Thrissur";
s_a[13] = "Balaghat|Barwani|Betul|Bharhut|Bhind|Bhojpur|Bhopal|Burhanpur|Chhatarpur|Chhindwara|Damoh|Datia|Dewas|Dhar|Dr. Ambedkar Nagar (Mhow)|Guna|Gwalior|Hoshangabad|Indore|Itarsi|Jabalpur|Jhabua|Khajuraho|Khandwa|Khargone|Maheshwar|Mandla|Mandsaur|Morena|Murwara|Narsimhapur|Narsinghgarh|Narwar|Neemuch|Nowgong|Orchha|Panna|Raisen|Rajgarh|Ratlam|Rewa|Sagar|Sarangpur|Satna|Sehore|Seoni|Shahdol|Shajapur|Sheopur|Shivpuri|Ujjain|Vidisha";
s_a[14] = "Ahmadnagar|Akola|Amravati|Aurangabad|Bhandara|Bhusawal|Bid|Buldhana|Chandrapur|Daulatabad|Dhule|Jalgaon|Kalyan|Karli|Kolhapur|Mahabaleshwar|Malegaon|Matheran|Mumbai|Nagpur|Nanded|Nashik|Qsmanabad|Pandharpur|Parbhani|Pune|Ratnagiri|Sangli|Satara|Sevagram|Solapur|Thane|Ulhasnagar|Vasai-Virar|Wardha|Yavatmal";
s_a[15] = "Imphal";
s_a[16] = "Cherrapunji|Shillong";
s_a[17] = "Aizawl|Lunglei";
s_a[18] = "Kohima|Mon|Phek|Wokha|Zunheboto";
s_a[19] = "Balangir|Baleshwar|Baripada|Bhubaneshwar|Brahmapur|Cuttack|Dhenkanal|Kendujhar|Konark|Koraput";
s_a[20] = "Amritsar|Batala|Chandigarh|Faridkot|Firozpur|Gurdaspur|Hoshiarpur|Jalandhar|Kapurthala|Ludhiana|Nabha";
s_a[21] = "Abu|Ajmer|Alwar|Amer|Aarmer|Beawar|Bharatpur|Bhilwara|Bikaner|Bundi|Chittaurgarh|Churu|Dhaulpur|Dungarpur|Ganganagar|Hanumangarh|Jaipur|Jaisalmer|Jalor|Jhalawar|Jhunjhunu|Jodhpur|Kishangarh|Kota|Merta|Nagaur|Nathdwara|Pali|Phalodi|Pushkar|Sawai Madhopur|Shahpura|Sikar";
s_a[22] = "Gangtok|Gyalshing|Lachung|Mangan";
s_a[23] = "Arcot|Chengalpattu|Chennai|Chidambaram|Coimbatore|Cuddalore|Dharmapuri|Dindigul|Erode|Kanchipuram|Kanniyakumari|Kodaikanal|Kumbakonam|Madurai|Mamallapuram|Nagappattinam|Nagercoil|Palayamkottai|Pudukkottai|Rajapalayam|Ramanathapuram|Salem|Thanjavur|Tiruchchirappalli|Tirunelveli|Tiruppur|Thoothukudi|Udhagamandalam|Vellore";
s_a[24] = "Hyderabad|Karimnagar|Khammam|Mahbubnagar|Nizamabad|Sangareddi|Warangal";
s_a[25] = "Agartala";
s_a[26] = "Agra|Aligarh|Amroha|Ayodhya|Azamgarh|Bahraich|Ballia|Banda|Bara Banki|Bareilly|Basti|Bijnor|Bithur\Budaun|Bulandshahr|Deoria|Etah|Etawah|Faizabad";
s_a[27] = "Almora|Dehra Dun|Haridwar|Mussoorie|Nainital|Pithoragarh";
s_a[28] = "Alipore|Alipur Duar|Asansol|Baharampur|Bally|Balurghat|Bankura|Baranagar|Barasat|Barrackpore|Basirhat|Bhatpara|Bishnupur|Budge Budge|Burdwan";
function print_state(state_id) {
    var option_str = document.getElementById(state_id);
    option_str.length = 0;
    option_str.options[0] = new Option('Select State', '');
    option_str.selectedIndex = 0;
    for (var i = 0; i < state_arr.length; i++) {
        option_str.options[option_str.length] = new Option(state_arr[i], state_arr[i])
    }
}

function print_city(city_id, city_index) {
    var option_str = document.getElementById(city_id);
    option_str.length = 0;
    option_str.options[0] = new Option('Select City', '');
    option_str.selectedIndex = 0;
    var city_arr = s_a[city_index].split("|");
    for (var i = 0; i < city_arr.length; i++) {
        option_str.options[option_str.length] = new Option(city_arr[i], city_arr[i])
    }
}