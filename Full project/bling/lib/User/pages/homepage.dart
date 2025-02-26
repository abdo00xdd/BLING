import 'package:flutter/material.dart';

class Homepage extends StatefulWidget {
  const Homepage({super.key});

  @override
  State<Homepage> createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  late String fullname;
  late int score;
  @override
  Widget build(BuildContext context) {
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
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    "$score",
                    style: TextStyle(
                      fontSize: 50,
                      fontWeight: FontWeight.bold,
                      color: Colors.black,
                    ),
                  ),
                ],
              ),
            ),
          ),
          Expanded(
              flex: 1,
              child: Container(
                color: Colors.red,
              )),
          Expanded(
              flex: 5,
              child: Container(
                color: Colors.yellow,
              )),
          Expanded(
              flex: 2,
              child: Container(
                color: Colors.purple,
              )),
        ],
      ),
    );
  }
}
