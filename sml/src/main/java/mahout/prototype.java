package mahout;

import java.io.File;
import java.io.IOException;
import java.util.List;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.eval.DataModelBuilder;
import org.apache.mahout.cf.taste.eval.RecommenderBuilder;
import org.apache.mahout.cf.taste.eval.RecommenderEvaluator;
import org.apache.mahout.cf.taste.impl.common.FastByIDMap;
import org.apache.mahout.cf.taste.impl.eval.AverageAbsoluteDifferenceRecommenderEvaluator;
import org.apache.mahout.cf.taste.impl.eval.RMSRecommenderEvaluator;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.neighborhood.NearestNUserNeighborhood;
import org.apache.mahout.cf.taste.impl.neighborhood.ThresholdUserNeighborhood;
import org.apache.mahout.cf.taste.impl.recommender.GenericUserBasedRecommender;
import org.apache.mahout.cf.taste.impl.similarity.PearsonCorrelationSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.TanimotoCoefficientSimilarity;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.model.PreferenceArray;
import org.apache.mahout.cf.taste.neighborhood.UserNeighborhood;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.recommender.Recommender;
import org.apache.mahout.cf.taste.recommender.UserBasedRecommender;
import org.apache.mahout.cf.taste.similarity.UserSimilarity;
import org.apache.mahout.common.RandomUtils;

public class prototype {

	public static void main(String[] args) throws TasteException {
		// TODO Auto-generated method stub

		
		try {
			final DataModel model = new FileDataModel(new File("/Users/aechelm/Documents/amazon_mahout.csv"));
			
			UserSimilarity similarity = new PearsonCorrelationSimilarity(model);
			
			UserNeighborhood neighborhood = new ThresholdUserNeighborhood(.01, similarity, model);
			
			UserBasedRecommender recommender = new GenericUserBasedRecommender(model, neighborhood, similarity);
			
			List<RecommendedItem> recommendations = recommender.recommend(1, 10);
			
			
			for (RecommendedItem recommendation : recommendations) {
			  System.out.println(recommendation);
			}

			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		String recsFile="/Users/aechelm/Documents/amazon_mahout.csv";
		final int neighbourhoodSize = 7;
		
        /*creating a RecommenderBuilder Objects with overriding the buildRecommender method
        this builder object is used as one of the parameters for RecommenderEvaluator - evaluate method*/
       
        //for Recommendation evaluations
        RecommenderBuilder userSimRecBuilder = new RecommenderBuilder() {
              public Recommender buildRecommender(DataModel model)throws TasteException
              {
                    //The Similarity algorithms used in your recommender
                    UserSimilarity userSimilarity = new TanimotoCoefficientSimilarity(model);
                   
                    /*The Neighborhood algorithms used in your recommender
                     not required if you are evaluating your item based recommendations*/
                    UserNeighborhood neighborhood =new NearestNUserNeighborhood(neighbourhoodSize, userSimilarity, model);
                   
                    //Recommender used in your real time implementation
                    Recommender recommender =new GenericUserBasedRecommender(model, neighborhood, userSimilarity);
                    return recommender;
              }
        };
       
        try {
             
              //Use this only if the code is for unit tests and other examples to guarantee repeated results
              RandomUtils.useTestSeed();
             
              //Creating a data model to be passed on to RecommenderEvaluator - evaluate method
              FileDataModel dataModel = new FileDataModel(new File(recsFile));
             
              /*Creating an RecommenderEvaluator to get the evaluation done
              you can use AverageAbsoluteDifferenceRecommenderEvaluator() as well*/
              RecommenderEvaluator evaluator = new RMSRecommenderEvaluator();
             
              //for obtaining User Similarity Evaluation Score
              double userSimEvaluationScore = evaluator.evaluate(userSimRecBuilder,null,dataModel, 0.7, 1.0);
              System.out.println("User Similarity Evaluation score : "+userSimEvaluationScore);
                                           
        } catch (IOException e) {
              // TODO Auto-generated catch block
              e.printStackTrace();
        } catch (TasteException e) {
              // TODO Auto-generated catch block
              e.printStackTrace();
        }
  }
		
		
}


