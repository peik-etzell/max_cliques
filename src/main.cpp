#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/bron_kerbosch_all_cliques.hpp>
#include <boost/graph/erdos_renyi_generator.hpp>
#include <boost/random/linear_congruential.hpp>
#include <iostream>

// https://www.boost.org/doc/libs/1_83_0/libs/graph/doc/erdos_renyi_generator.html
// ^ Example constructing ER graph
typedef boost::adjacency_list<> Graph;
typedef boost::erdos_renyi_iterator<boost::minstd_rand, Graph> ERGen;

static const float p = 0.5;

int main(int argc, char** argv) {
    boost::minstd_rand gen;

#pragma omp parallel for schedule(dynamic, 1)
    for (int n = 2; n < 500; ++n) {
        Graph G(ERGen(gen, n, p), ERGen(), n);
        int omega = boost::bron_kerbosch_clique_number(G);
#pragma omp critical
        { std::cout << n << '\t' << omega << std::endl; }
    }

    return 0;
}
