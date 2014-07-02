#include <iostream>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

template <class T>
class Node {
  char character;
  vector<T> docs;
  map<char, Node*> children;
public:
  Node(char c) { character = c; };
  char getChar() { return character; };
  bool hasChild(char);
  bool hasChildren();
  Node* getChild(char);
  map<char, Node*> getChildren();
  Node* makeChild(char);
  void insertDocNum(T);
  vector<T> getDocs();

  friend ostream& operator<<(ostream& os, Node<int>& node) {
    os << node.character << ": ";
    for (vector<int>::iterator it = node.docs.begin(); it != node.docs.end(); ++it) {
      os << *it << " ";
    }
    return os;
  };

  /*friend ostream& operator<<(ostream& os, Node<string>& node) {
    os << node.character << ": ";
    for (vector<string>::iterator it = node.docs.begin(); it != node.docs.end(); ++it) {
      os << *it << " ";
    }
    return os;
  } */
};

template <class T>
bool Node<T>::hasChild(char letter) {
  if (children.count(letter) == 1) {
    return true;
  }
  else {
    return false;
  }
}

template <class T>
bool Node<T>::hasChildren() {
  if (children.empty()) {
    return false;
  }
  else {
    return true;
  }
}

template <class T>
Node<T>* Node<T>::getChild(char letter) {
  return children[letter];
}

template <class T>
Node<T>* Node<T>::makeChild(char letter) {
  children[letter] = new Node(letter);

  // returns for later use
  return children[letter];
}

template <class T>
void Node<T>::insertDocNum(T docName) {
  docs.push_back(docName);
}

template <class T>
vector<T> Node<T>::getDocs() {
  return docs;
}

template <class T>
class Trie {
  Node<T>* root;
  void recursiveStatisticsPrinting(Node<T>*, int, string);
  int maximumDepth;
  string maximumDepthWord;
  int maxNodeChildren;
  Node<T>* maxNodeChildrenNode;
public:
  Trie<T>() { root = new Node<T>(' '); };
  void insert(string, T);
  vector<T> search(string);
  void printStatistics();
};

template <class T>
void Trie<T>::insert(string key, T docName) {
  char letter;
  bool found;

  // sets iterator node to the root of the trie
  Node<T>* iterNode = root;

  // Bool test for insertion (key is depleted of characters)
  while (key != "") {
    // Take first letter
    letter = key[0];

    // Take everything from index 1 onwards
    key = key.substr(1);


    found = iterNode->hasChild(letter);

    if (found) {
      iterNode = iterNode->getChild(letter);
    }
    else {
      iterNode = iterNode->makeChild(letter);
    }
  }
  // Once letters are depleted, doc is inserted
  iterNode->insertDocNum(docName);
}

template <class T>
vector<T> Trie<T>::search(string key) {
  // Empty vector for false result
  vector<T> falseVector;

  // Iterator node
  Node<T>* iterNode = root;

  // Bool test for if chilldren of iterNode are found
  bool found = false;
  // Bool for while loop end conditions - end of tree = leaf
  bool atEnd = false;
  char letter;

  while (!atEnd and key != "") {
    // Take first letter
    letter = key[0];
    // Take everything from index 1 onwards
    key = key.substr(1);

    found = iterNode->hasChild(letter);


    if (found) {
      iterNode = iterNode->getChild(letter);
    }
    else {
      atEnd = true;
    }
  }

  // If the key has been depleted (the word has been found completely) and the docs exist
  if (key == "" and !iterNode->getDocs().empty()) {
    iterNode->getDocs();
  }
  else {
    return falseVector;
  }
}

template <class T>
void Trie<T>::printStatistics() { // Shell method for recursion call

  this->recursiveStatisticsPrinting(root, 0, "");

  // TODO: GET THIS WORKING!

  cout << this->maximumDepth << this->maximumDepthWord << endl;
  cout << this->maxNodeChildren << this->maxNodeChildrenNode << endl;
}

template <class T>
void Trie<T>::recursiveStatisticsPrinting(Node<T>* iterNode, int currentDepth, string lettersSoFar) {

  string word = lettersSoFar + iterNode->getChar();

  // Base case
  if (!iterNode->hasChildren()) {
    if (currentDepth > this->maximumDepth) {
      this->maximumDepth = currentDepth;
      this->maximumDepthWord = word;
    }
    return;
  }

  // Recursion
  else {
    // If statement to output all words and their doc counts to a .csv, for processing with Excel
    /*if (iterNode->hasChildren()) {
      string comma = ",";

      os << iterNode->getChildren().size();
      os << ",";
      os << word;
      os << "\n";
    }*/

    // Updating the Trie's max depth (largest key)
    if (currentDepth != 0 and iterNode->hasChildren()) {
      if (iterNode->getChildren().size() > this->maxNodeChildren) {
        this->maxNodeChildren = iterNode->getChildren().size();
        this->maxNodeChildrenNode = iterNode;
      }
    }


    map<char, Node<T>*> childrenMap = iterNode->getChildren();

    // Continue recursion
    for (typename map<char, Node<T>*>::iterator it = childrenMap.begin(); it != childrenMap.end(); it++) {
      Node<T> iter = *it->second;
      // Recursive call
      this->recursiveStatisticsPrinting(&iter, currentDepth + 1, word);
    }
  }
}

int main() {
  Trie<int>* trie = new Trie<int>();

	trie->insert("apple", 1);
  trie->insert("appley", 4);
  trie->insert("apple", 6);
  trie->insert("apple", 2);

  vector<int> docs = trie->search("apple");

  cout << "Apple found in docs: ";

  for (vector<int>::iterator it = docs.begin(); it != docs.end(); ++it) {
    cout << *it << " ";
  }

  cout << endl;

  trie->printStatistics();

  // AAN Trie
  /*Trie<int>* aanTrie = new Trie<int>();
  ifstream fin;

  fin.open("/home/bryan/Desktop/Wheaton-116/word-files.csv");
  string line;
  string word;
  string tempDoc;
  int doc;
  int splitIndex;

  if (fin.is_open()) {
    while (fin.good()) {
      getline(fin, line);
      istringstream liness(line);

      getline(liness, word, ',');
      getline(liness, tempDoc, ',');

      doc = atoi(tempDoc.c_str());

      aanTrie->insert(word, doc);
    }
  } */
}