package go.games.selenium.test;

import java.time.Duration;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.Select;
import java.util.concurrent.TimeUnit;

public class TestScript {

    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "C:\\selenium webdriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        
        //lOG IN
        driver.get("https://pixie-pia.web.app/login");
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(60));
        
        // Wait for the email input field to be visible
        WebElement emailInput = wait.until(ExpectedConditions.elementToBeClickable(By.name("email")));
        emailInput.sendKeys("mansib@gmail.com");

        // Find the password input field and enter password
        WebElement passwordInput = driver.findElement(By.name("password"));
        passwordInput.sendKeys("Mansib123#");
        
        // Click on the login button
        driver.findElement(By.xpath("//*[@id=\"root\"]/div/main/div/div/form/div[4]/button")).click();
        
        
        try {
            Thread.sleep(5000); // Sleep for 5 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        // ADD TOY 
        driver.navigate().to("https://pixie-pia.web.app/addtoy");
        
//        WebElement addToyLink = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"root\"]/div/div[1]/div[2]/ul/a[1]")));
//        addToyLink.click();  
        
        try {
            Thread.sleep(5000); // Sleep for 5 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        // Fill in toy details
        driver.findElement(By.name("toyName")).sendKeys("Cowboy");
        driver.findElement(By.name("price")).sendKeys("5");
        
        Select select = new Select(wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"root\"]/div/main/form/div[1]/div[3]/select"))));
        select.selectByVisibleText("Playsets");
        
        Select select1 = new Select(wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"root\"]/div/main/form/div[1]/div[4]/select"))));
        select1.selectByVisibleText("Toy Story Playset");        
        
        WebElement m = driver.findElement(By.xpath("//*[@id=\"root\"]/div/main/form/div[1]/div[5]/textarea"));
        m.sendKeys("Toy");
        
        WebElement n = driver.findElement(By.xpath("//*[@id=\"root\"]/div/main/form/div[1]/div[6]/textarea"));
        n.sendKeys("Very good");
      
        driver.findElement(By.name("availableQuantity")).sendKeys("5");
        driver.findElement(By.name("pictureUrl")).sendKeys("https://i5.walmartimages.com/seo/Award-Winning-Disney-Pixar-Toy-Story-4-Woody-And-Buzz-Lightyear-2-Character-Pack-Movie-Inspired-Relative-Scale-For-Storytelling-Play_c5719fb2-ffe3-47ab-849f-840409636c0a_1.a24a047099e9e0740e47177ecd67d45d.jpeg");
        driver.findElement(By.name("rating")).sendKeys("5");
        driver.findElement(By.name("brand")).sendKeys("disney");
        driver.findElement(By.name("ageRange")).sendKeys("3-6");
        driver.findElement(By.name("material")).sendKeys("Plastic");
        driver.findElement(By.name("weight")).sendKeys("200gm");
        driver.findElement(By.name("color")).sendKeys("Yellow Blue");
        driver.findElement(By.name("countryOfOrigin")).sendKeys("Usa");
        
        // Click on the add toy button
        WebElement addToyButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"root\"]/div/main/form/div[2]/button")));
        addToyButton.click();
        
        //View my Toy List
        driver.navigate().to("https://pixie-pia.web.app/mytoys");
        
        
        try {
            Thread.sleep(5000); // Sleep for 5 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        //Delete Toy
        WebElement deleteToyButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"root\"]/div/main/div/div/table/tbody/tr[3]/td[7]/div[3]")));
        deleteToyButton.click();
        
        
        WebElement confirmDelete = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/div[2]/div/div[6]/button[1]")));
        confirmDelete.click();
        
        WebElement confirmDeletef = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/div[2]/div/div[6]/button[1]")));
        confirmDeletef.click();
        
        
        try {
            Thread.sleep(5000); // Sleep for 5 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
      //Update mytoy details
        WebElement editToyButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"root\"]/div/main/div/div/table/tbody/tr[1]/td[7]/div[2]/a/button")));
        editToyButton.click();
        
        
        try {
            Thread.sleep(5000); // Sleep for 5 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        driver.findElement(By.name("toyName")).sendKeys("Barbie");
        driver.findElement(By.name("price")).sendKeys("2");
        Select select2 = new Select(wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"root\"]/div/main/div/div/form/div[1]/div[3]/select"))));
        select.selectByVisibleText("Dolls");
        
        Select select3 = new Select(wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"root\"]/div/main/div/div/form/div[1]/div[4]/select"))));
        select1.selectByVisibleText("Princess Dolls");
        
        WebElement updateToyButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"root\"]/div/main/div/div/form/div[2]/button")));
        updateToyButton.click();
      
      
        
       
//        driver.quit();
        
    }
}
