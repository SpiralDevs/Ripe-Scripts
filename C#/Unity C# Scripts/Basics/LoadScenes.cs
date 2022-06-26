using UnityEngine;
using UnityEngine.SceneManagement; // This is what we HAVE to use in order to switch scenes

public class LoadScenes : MonoBehaviour 
{
    public void SceneString()
    {
        /*Loading Example 1: String */ SceneManager.LoadScene("SampleScene")//place the name of the scene you want to use in the quotations
    }
    public void SceneInt()
    {
        /*Loading Example 2: Int/Build Index*/ SceneManager.LoadScene(1)//In the parentheses is the build index of the scene in File > Build Settings
    }

    void Start()
    {
        SceneString();
        // SceneInt();
    }
}