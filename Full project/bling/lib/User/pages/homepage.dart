import 'package:carousel_slider/carousel_slider.dart';
import 'package:flutter/material.dart';

class Homepage extends StatefulWidget {
  const Homepage({super.key});

  @override
  State<Homepage> createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  late String fullname;
  late int score;
  late String qoute;
  late List<Widget> announces = [];
  @override
  Widget build(BuildContext context) {
    qoute = "The only way to do great work is to love what you do";
    announces.add(
      Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        margin: EdgeInsets.all(10),
        color: Colors.teal,
        child: Text("Announce 1"),
      ),
    );
    announces.add(
      Container(
        width: MediaQuery.of(context).size.width + 100,
        height: MediaQuery.of(context).size.height + 100,
        margin: EdgeInsets.all(10),
        color: Colors.yellow,
        child: Text("Announce 2"),
      ),
    );
    announces.add(
      Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        margin: EdgeInsets.all(10),
        color: Colors.green,
        child: Text("Announce 3"),
      ),
    );
    announces.add(
      Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        margin: EdgeInsets.all(10),
        color: Colors.greenAccent,
        child: Text("Announce 4"),
      ),
    );
    announces.add(
      Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        margin: EdgeInsets.all(10),
        color: Colors.purple,
        child: Text("Announce 5"),
      ),
    );
    announces.add(
      Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        margin: EdgeInsets.all(10),
        color: Colors.redAccent,
        child: Text("Announce 6"),
      ),
    );
    announces.add(
      Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        margin: EdgeInsets.all(10),
        color: Colors.blue,
        child: Text("Announce 7"),
      ),
    );
    announces.add(
      Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        margin: EdgeInsets.all(10),
        color: Colors.lightBlueAccent,
        child: Text("Announce 8"),
      ),
    );
    fullname = "Rida ELANTARI";
    score = 100;
    return SafeArea(
      child: Column(
        children: [
          Expanded(
            // For Search and notification
            flex: 1,
            child: Padding(
              padding: EdgeInsets.all(10),
              child: Row(
                children: [
                  Expanded(
                    // Search
                    flex: 12,

                    child: TextField(
                      decoration: InputDecoration(
                        filled: true,
                        hintText: "Search",
                        contentPadding: EdgeInsets.symmetric(
                            vertical: 0.0), // Adjust this value as needed
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(10),
                          borderSide: BorderSide.none,
                        ),
                        prefixIcon: Icon(Icons.search, color: Colors.black),
                      ),
                    ),
                  ),
                  Expanded(
                    flex: 2,
                    child: Container(
                      width: 50,
                      height: 50,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        color: Colors.transparent,
                      ),
                      child: IconButton(
                        icon: Icon(Icons.message, color: Colors.black),
                        onPressed: () {
                          print("Notification");
                        },
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
          Expanded(
            flex: 1,
            child: Row(
              children: [
                Padding(
                  padding: EdgeInsets.all(15),
                  child: Text(
                    "Welcome, $fullname",
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontSize: 23,
                      fontWeight: FontWeight.bold,
                      color: Colors.grey,
                    ),
                  ),
                ),
              ],
            ),
          ),
          Expanded(
            flex: 1,
            child: Row(
              children: [
                Padding(
                  padding: EdgeInsets.all(15),
                  child: Text(
                    "Score: ",
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: Colors.black,
                    ),
                  ),
                ),
              ],
            ),
          ),
          Expanded(
            flex: 2,
            child: Center(
              child: Padding(
                padding: EdgeInsets.symmetric(horizontal: 50),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [
                    Text(
                      "$score",
                      style: TextStyle(
                        fontFamily: 'Inter',
                        fontSize: 50,
                        fontWeight: FontWeight.bold,
                        color: Colors.black,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
          Expanded(
            flex: 1,
            child: Row(
              children: [
                Padding(
                  padding: EdgeInsets.all(15),
                  child: Text(
                    "Anonces: ",
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: Colors.black,
                    ),
                  ),
                ),
              ],
            ),
          ),
          Expanded(
            flex: 7, //Annconce
            child: CarouselSlider(
              items: announces,
              options: CarouselOptions(
                initialPage: 0,
                autoPlay: true,
              ),
            ),

            // width: 400,
          ),
          Expanded(
            flex: 2,
            child: Container(
              margin: EdgeInsets.all(10),
              padding: EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: const Color.fromARGB(255, 220, 205, 159),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Center(
                child: Text(
                  'The qoute of the day: " $qoute " ',
                  style: TextStyle(
                    fontFamily: 'Merriweather',
                    fontSize: 15,
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
