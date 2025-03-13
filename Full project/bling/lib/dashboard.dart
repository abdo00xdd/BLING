import 'package:curved_navigation_bar/curved_navigation_bar.dart';
import 'package:flutter/material.dart';

import 'User/pages.dart';

class Dashboard extends StatefulWidget {
  @override
  _DashboardState createState() => _DashboardState();
}

class _DashboardState extends State<Dashboard> {
  // const Dashboard({super.key});
  int pageIndex = 0;
  // This widget is the root of your application.
  void changeIndex(int i) {}
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      body: SafeArea(
        child: Column(
          children: [
            Expanded(flex: 22, child: pages[pageIndex]),
          ],
        ),
      ),
      backgroundColor: Colors.white,
      bottomNavigationBar: CurvedNavigationBar(
        buttonBackgroundColor: Colors.white,
        backgroundColor: Colors.white,
        color: Colors.black12,
        onTap: (i) {
          setState(() {
            pageIndex = i;
          });
        },
        items: [
          Icon(Icons.home),
          Icon(Icons.calculate),
          Icon(Icons.alarm),
          Icon(Icons.message),
          Icon(Icons.person),
        ],
      ),
    );
  }
}
