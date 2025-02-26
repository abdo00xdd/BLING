import 'package:flutter/material.dart';

import 'User/pages.dart';

class Dashboard extends StatelessWidget {
  const Dashboard({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Column(
          children: [
            Expanded(flex: 22, child: pages[0]),
            Expanded(flex: 2, child: Container(color: Colors.blue)),
          ],
        ),
      ),
    );
  }
}
