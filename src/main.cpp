#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/bron_kerbosch_all_cliques.hpp>
#include <boost/graph/erdos_renyi_generator.hpp>
#include <boost/random/linear_congruential.hpp>
#include <iostream>
#include <ostream>

// https://www.boost.org/doc/libs/1_83_0/libs/graph/doc/erdos_renyi_generator.html
// ^ Example constructing ER graph
typedef boost::adjacency_list<> Graph;
typedef boost::erdos_renyi_iterator<boost::minstd_rand, Graph> ERGen;

static const float P = 0.5;

int main(int argc, char** argv) {
    boost::minstd_rand gen;

    for (int n = 10; n < 500; ++n) {
        Graph G(ERGen(gen, n, P), ERGen(), 100);
        int omega = boost::bron_kerbosch_clique_number(G);
        std::cout << "Clique number of graph G(" << n << ", " << P
                  << "): " << omega << std::endl;
    }

    return 0;
}
