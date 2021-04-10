#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include <ctime>
#include <fstream>
#include <string>
#include <iomanip>

void print(const std::vector<int>& v)
{
	for (int e : v) {
		std::cout << " " << e;
	}
	std::cout << std::endl;
}

int cost(const std::vector<int>& perm, const std::vector<int>& dates, const std::vector<int>& prios, const int d) {
	int sum = 0, tmp = 0;
	for (int i = 0; i < perm.size(); i++) {
		tmp = 0;
		for (int j = 0; j <= i; j++) {
			tmp += dates[perm[j]];
		}
		sum += prios[perm[i]] * std::abs(tmp - d);
	}
	return sum;
}

int start(const std::vector<int>& perm, const std::vector<int>& dates, const std::vector<int>& prios, const int total) {
	int date = 0, prio = 0;
	for (int i = 0; 2*prio <= total; i++) {
		prio += prios[perm[i]];
		date += dates[perm[i]];
	}
	return date;
}

unsigned long long fact(int n) {
	if (n < 2) return 1;
	if (n == 2) return 2;
	return n*fact(n-1);
}
	
int main(int argc, char *argv[])
{
	srand (time(NULL));
	int n = 0;
	unsigned long long permsn = 0;
	if (argc == 2) {
		n = atoi(argv[1]);
	} else {
		std::cin >> n;
	}
	permsn = (float) fact(n);
	std::vector<int> sigma = {}, dates = {}, prio = {};
	for (int i = 0; i < n; i++) {
		sigma.push_back(i);
		dates.push_back(rand() % 20 + 1);
		prio.push_back(rand() % 20 + 1);
	}
	int total = 0;
	for(std::vector<int>::iterator it = prio.begin(); it != prio.end(); ++it)
    	total += *it;
	
	int min = -1, co = 0, st = 0, minSt = 0, resn = 0;
	std::vector<std::vector<int>> minPerms = {};
	std::vector<int> minSts = {};
	bool diff = true;
	// vector should be sorted at the beginning.

	long count = 0;
	float progress = 0;
	std::time_t startingTime = std::time(nullptr);
	do {
		count++;
		st = start(sigma, dates, prio, total);
		co = cost(sigma, dates, prio, st);
		if (min == -1 || co < min) {
			min = co;
			diff = true;
			minSt = st;
			resn = 1;
			minPerms = { sigma };
			minSts = { st };
		} else if (min == co) {
			if (minSt != st) diff = false;
			minPerms.push_back(sigma);
			minSts.push_back(st);
			resn++;
		}
		if (count%100000 == 0) {
			// std::cout << count << " " << permsn << std::endl;
			int barWidth = 70;
			std::time_t currentTime = std::time(nullptr);

			progress = (float)count/(float)permsn;

			int rest = (float) (currentTime - startingTime) * ( 1.0 / progress - 1 );

			std::cout << "[";
			int pos = barWidth * progress;
			for (int i = 0; i < barWidth; ++i) {
				if (i < pos) std::cout << "=";
				else if (i == pos) std::cout << ">";
				else std::cout << " ";
			}
			std::cout << "] " << int(progress * 100.0) << " % (" << count << '/' << permsn << ") " << rest << "sec restantes \r";
			std::cout.flush();
		}
	} while (std::next_permutation(sigma.begin(), sigma.end()));

	// int minSt = minSts[0];
	// for (int i = 0; i < minSts.size(); i++) {
	// 	if (minSts[i] != minSt) {
	// 		std::cout << "FALSE " << minSts[i] << " != " << minSt << std::endl;
	// 	}
	// }
	std::cout.flush();
	if (diff) {
		std::cout << "\n The prophecy is true" << std::endl;
	} else {
		std::cout << "\n You are a fucking idiot" << std::endl;
	}
	std::cout << resn << " minimals" << std::endl;
	std::stringstream time;
	time << std::put_time(std::localtime(&startingTime), "%Y%m%d%H%I%M%S");
	std::string fileName = "tfjm_"+ std::to_string(n)+'_' + time.str();
	std::cout << fileName << std::endl;
	std::ofstream Result("data/"+fileName);
	int el = 0;
	for (int i = 0; i < minPerms.size(); i++) {
		std::cout << i <<"eme was : ";
		Result << '[';
		for (int j = 0; j < minPerms[i].size() - 1; j++) {
			el = minPerms[i][j];
			std::cout << '(' << prio[el] << ", " << dates[el] << ") " << (float)prio[el]/(float)dates[el] << " ";
			Result << '(' << prio[el] << ", " << dates[el] << "), ";
		}
		el = minPerms[i][minPerms[i].size() - 1];
		std::cout << '(' << prio[el] << ", " << dates[el] << ") " << (float)prio[el]/(float)dates[el] << "\n\t with start from -" << minSts[i] << std::endl;
		Result << '(' << prio[el] << ", " << dates[el] << ")];" << minSts[i] << std::endl;
	}
	// Result << minSt << std::endl;
	Result.close();
	return 0;
}