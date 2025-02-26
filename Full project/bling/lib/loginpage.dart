import 'package:flutter/material.dart';

class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: PreferredSize(
        preferredSize: Size.fromHeight(70.0), // Height of the AppBar
        child: Container(
          decoration: BoxDecoration(
            color: const Color.fromARGB(
                255, 255, 255, 255), // AppBar background color
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              SizedBox(
                width: 20,
              ),
              Icon(
                Icons.abc,
                size: 70,
              ),
              Center(
                child: Text(
                  "",
                  style: TextStyle(
                    color: const Color.fromARGB(255, 0, 0, 0),
                    fontSize: 20.0,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              Icon(
                Icons.abc,
                size: 0,
              ),
            ],
          ),
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text(
              "Log In",
              style: TextStyle(
                fontFamily: 'Ubuntu',
                fontWeight: FontWeight.bold,
                fontSize: 35,
              ),
            ),
            SizedBox(
              height: 20,
            ),
            SizedBox(
              width: 300, // Set the desired width
              child: Column(
                children: [
                  TextField(
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Usernam',
                      hintText: 'Type your usernam',
                      prefixIcon: Icon(Icons.person), // Icon on the left
                    ),
                  ),
                  SizedBox(
                    height: 9,
                  ),
                  TextField(
                    obscureText: true,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Password',
                      hintText: 'Type your Password',
                      prefixIcon: Icon(Icons.lock), // Icon on the left
                    ),
                  ),
                  SizedBox(
                    height: 8,
                  ),
                  Row(
                    children: [
                      Text(
                        "Or create account from ",
                        style: TextStyle(
                          fontFamily: 'Ubuntu',
                        ),
                      ),
                      TextButton(
                          onPressed: () {},
                          child: Text("here",
                              style: TextStyle(
                                  color: Colors.blueAccent,
                                  fontFamily: 'Ubuntu')))
                    ],
                  ),
                  SizedBox(
                    width: 300,
                    child: ElevatedButton.icon(
                      onPressed: () {},
                      iconAlignment: IconAlignment.start,
                      label: Text(
                        "LogIn",
                        style: TextStyle(
                            color: const Color.fromARGB(255, 255, 255, 255),
                            fontSize: 15,
                            fontFamily: 'Ubuntu'),
                      ),
                      icon: Icon(
                        Icons.key,
                        color: Colors.white,
                      ),
                      style: ElevatedButton.styleFrom(
                        elevation: 10.0,
                        backgroundColor: const Color.fromARGB(
                            255, 0, 0, 0), // Background color
                        foregroundColor: Colors.white, // Text and icon color
                        shape: RoundedRectangleBorder(
                          borderRadius:
                              BorderRadius.circular(23), // Rounded corners
                        ),
                        padding: EdgeInsets.symmetric(
                            horizontal: 20, vertical: 12), // Padding
                      ),
                    ),
                  ),
                  Text(
                    "OR",
                    style: TextStyle(
                        color: const Color.fromARGB(255, 0, 0, 0),
                        fontSize: 15,
                        fontFamily: 'Ubuntu'),
                  ),
                  SizedBox(
                    width: 300,
                    child: ElevatedButton.icon(
                      onPressed: () {},
                      iconAlignment: IconAlignment.start,
                      label: Text(
                        "Google",
                        style: TextStyle(
                            color: const Color.fromARGB(255, 0, 0, 0),
                            fontSize: 15,
                            fontFamily: 'Ubuntu'),
                      ),
                      icon: Icon(
                        Icons.mail,
                        color: const Color.fromARGB(255, 0, 0, 0),
                      ),
                      style: ElevatedButton.styleFrom(
                        elevation: 10.0,
                        backgroundColor: const Color.fromARGB(
                            255, 255, 255, 255), // Background color
                        foregroundColor: const Color.fromARGB(
                            255, 0, 0, 0), // Text and icon color
                        shape: RoundedRectangleBorder(
                          side: BorderSide(color: Colors.black, strokeAlign: 1),
                          borderRadius:
                              BorderRadius.circular(23), // Rounded corners
                        ),
                        padding: EdgeInsets.symmetric(
                            horizontal: 20, vertical: 12), // Padding
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: Container(
        color: Colors.grey[200],
        padding: EdgeInsets.all(10),
        child: Text(
          "Version 1.0.0 - Copyright  2024",
          textAlign: TextAlign.center,
          style: TextStyle(
            fontSize: 14,
            color: Colors.grey[600],
          ),
        ),
      ),
    );
  }
}
