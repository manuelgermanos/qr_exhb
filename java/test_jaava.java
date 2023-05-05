import org.bson.Document;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import javax.servlet.http.HttpSession;
import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import static com.mongodb.client.model.Filters.eq;

@SpringBootApplication
@RestController
public class F1App {
    public static void main(String[] args) {
        SpringApplication.run(F1App.class, args);
    }

    private MongoClient mongoClient;
    private MongoDatabase database;
    private MongoCollection<Document> constructors;
    private MongoCollection<Document> drivesFor;
    private MongoCollection<Document> drivers;
    private MongoCollection<Document> rec1;

    public F1App() {
        mongoClient = new MongoClient("mongodb+srv://rec1:rec1@coe416database.qlhbx66.mongodb.net/");
        database = mongoClient.getDatabase("f1_2");
        constructors = database.getCollection("constructors");
        drivesFor = database.getCollection("drivesFor");
        drivers = database.getCollection("drivers");
        rec1 = database.getCollection("rec1");
    }

    @GetMapping("/constructor/{constID}")
    public String constructor(@PathVariable String constID, HttpSession session) {
        Document constructor_data = constructors.find(eq("constID", constID)).projection(new Document("_id", 0)).first();
        if (constructor_data == null) {
            return "{\"error\": \"Invalid constID\"}";
        }
        List<Document> drivesFor_data = drivesFor.find(eq("constID", constID)).projection(new Document("_id", 0).append("driverID", 1)).into(new ArrayList<>());
        List<Document> drivers_data = new ArrayList<>();
        for (Document driveFor : drivesFor_data) {
            Document driver_data = drivers.find(eq("driverID", driveFor.getString("driverID"))).projection(new Document("_id", 0)).first();
            if (driver_data != null) {
                drivers_data.add(driver_data);
            }
        }
        String prev_constID = (String)session.getAttribute("prev_constID");
        if (prev_constID != null && !prev_constID.equals(constID)) {
            String trans = prev_constID + "xx" + constID;
            rec1.updateOne(eq("trans", trans), new Document("$inc", new Document("num", 1)), new UpdateOptions().upsert(true));
        }
        Document doc = rec2.find(eq("picked", constID)).first();
        if (doc != null) {
            rec2.updateOne(eq("_id", doc.getObjectId("_id")), new Document("$inc", new Document("num1", 1)));
        }
        session.setAttribute("prev_constID", constID);
        Document data = new Document("constructor", constructor_data).append("drivers", drivers_data);
        return data.toJson();
    }
}
