// localmotifclustermain.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include "localmotifcluster.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main(int argc, char *argv[])
{
  Env = TEnv(argc, argv, TNotify::StdNotify);
  Env.PrepArgs(TStr::Fmt("Local motif clustering. build: %s, %s. Time: %s",
                         __TIME__, __DATE__, TExeTm::GetCurTm()));
  TExeTm ExeTm;
  Try

      const bool IsDirected =
          Env.GetIfArgPrefixBool("-d:", true, "Directed graph?");

  ProcessedGraph graph_p;
  if (IsDirected)
  {
    const TStr graph_filename =
        Env.GetIfArgPrefixStr("-i:", "C-elegans-frontal.txt", "Input graph file");
    const TStr motif =
        Env.GetIfArgPrefixStr("-m:", "triad", "Motif type");
    MotifType mt = ParseMotifType(motif, IsDirected);
    PNGraph graph;
    if (graph_filename.GetFExt().GetLc() == ".ngraph")
    {
      TFIn FIn(graph_filename);
      graph = TNGraph::Load(FIn);
    }
    else if (graph_filename.GetFExt().GetLc() == ".ungraph")
    {
      TExcept::Throw("Warning: input graph is an undirected graph!!");
    }
    else
    {
      graph = TSnap::LoadEdgeList<PNGraph>(graph_filename, 0, 1);
    }
    TSnap::DelSelfEdges(graph);
    graph_p = ProcessedGraph(graph, mt);
  }
  else
  {

    const TStr graph_filename =
        Env.GetIfArgPrefixStr("-i:", "C-elegans-frontal.txt", "Input graph file");
    const TStr motif =
        Env.GetIfArgPrefixStr("-m:", "clique3", "Motif type");
    MotifType mt = ParseMotifType(motif, IsDirected);
    PUNGraph graph;
    if (graph_filename.GetFExt().GetLc() == ".ungraph")
    {
      TFIn FIn(graph_filename);
      graph = TUNGraph::Load(FIn);
    }
    else if (graph_filename.GetFExt().GetLc() == ".ngraph")
    {
      TExcept::Throw("Warning: input graph is a directed graph!!");
    }
    else
    {
      graph = TSnap::LoadEdgeList<PUNGraph>(graph_filename, 0, 1);
    }
    TSnap::DelSelfEdges(graph);
    graph_p = ProcessedGraph(graph, mt);
  }

  // const TInt seed =
  //     Env.GetIfArgPrefixInt("-s:", 1, "Seed");
  const TFlt alpha =
      Env.GetIfArgPrefixFlt("-a:", 0.98, "alpha");
  const TFlt eps =
      Env.GetIfArgPrefixFlt("-e:", 0.0001, "eps");

  // for seed set
  // const TStr seeds_filename =
  //     Env.GetIfArgPrefixStr("-ss:", "/home/sfy/Documents/VScodeProject/SNAPro/Expriment/testComu.txt", "Input community");

  // transfer the true community ine by line into int so that afterwards can deal with thay.lllll
  std::ifstream infile("/home/sfy/Documents/testSNA/SNAPro/TruLocal.txt");
  std::vector<std::vector<int> > vv;

  if (infile.is_open())
  {
    for (std::string line; getline(infile, line);)
    {
      std::vector<int> v;

      int f;                      /* declare int */
      std::stringstream ss(line); /* make stringstream from s */
      while ((ss >> f))           /* read ints from ss into f */
        v.push_back(f);           /* add f to vector */

      vv.push_back(v);
    }
    std::ofstream Myfile;
    Myfile.open("outputComu.txt", std::ios_base::app);
    // std::cout << vv.size() << std::endl;

    // for (auto v_ : vv)
    for (int comm = 0; comm < vv.size(); comm++)
    {
      // printf("Size of Comunity: %d.\n", vv.size());
      if ((comm%100)==0)
      {
        printf("Begin community %d\n", comm);
      }

      for (int el = 0; el < vv[comm].size(); el++)
      {
        int seed = vv[comm][el];
        // printf("seed:%d.\n",seed);

        MAPPR mappr;
        mappr.computeAPPR(graph_p, seed, alpha, eps / graph_p.getTotalVolume() * graph_p.getTransformedGraph()->GetNodes());
        mappr.sweepAPPR(-1);
        Myfile << mappr.printCond() << " ";

        const TIntV cluster = mappr.getCluster();

        for (int clu = 0; clu < cluster.Len(); clu++)
        {

          Myfile << cluster.GetVal(clu) << " ";

          // printf("seed: %d. Cluster: %d.\n", seed, cluster.GetVal(clu));
        }
        // finish one seed clusters document
        Myfile << ",";
      }
      // finish one comunity clusters;
      Myfile << ";";
    }
  }
  Catch
      printf("\nrun time: %s (%s)\n", ExeTm.GetTmStr(),
             TSecTm::GetCurTm().GetTmStr().CStr());
  return 0;
}
