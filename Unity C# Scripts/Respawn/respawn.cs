using UnityEngine;
using UnityEngine.SceneManagement;

public class respawn : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        SceneManager.LoadScene("SCENE NAME HERE");
    } 
}