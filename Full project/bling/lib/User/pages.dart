import 'package:bling/User/pages/homepage.dart';
import 'package:flutter/material.dart';

List<Widget> pages = [
  Homepage(),
  Text("Calculator"),
  Text("Time management"),
  Text("Chat"),
  Text("Profile"),
];

var tabs = [
  Onglets(icon: Icons.home, name: "Home Page"),
  Onglets(icon: Icons.calculate, name: "Calculator"),
  Onglets(icon: Icons.timer, name: "Home Page"),
  Onglets(icon: Icons.chat, name: "Chat Rooms"),
  Onglets(icon: Icons.home, name: "Home Page"),
  Onglets(icon: Icons.person, name: "Profile"),
];

class Onglets {
  final IconData icon;
  final String name;

  const Onglets({required this.icon, required this.name});
}
